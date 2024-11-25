import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
    UpdateView,
)

from . import forms, models, services

logger = logging.getLogger(__name__)


class ServersMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if "server_pk" in self.kwargs:
            server = models.Server.objects.get(pk=self.kwargs["server_pk"])
            self.server = server
            if request.user in server.members.all():
                return super().dispatch(request, *args, **kwargs)
            if server.owner == request.user:
                return super().dispatch(request, *args, **kwargs)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servers"] = models.Server.objects.filter(
            Q(owner=self.request.user) | Q(members=self.request.user)
        ).distinct()
        if "server_pk" in self.kwargs:
            context["current_server"] = self.server
        else:
            context["channels"] = services.get_direct_message_channels(
                self.request.user
            )
        return context


class ServerMemberMixin:
    def dispatch(self, request, *args, **kwargs):
        if "server_pk" in self.kwargs:
            if request.user in self.server.members.all():
                return super().dispatch(request, *args, **kwargs)
            if self.server.owner == request.user:
                return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404


class ServerOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        server = models.Server.objects.get(pk=self.kwargs["server_pk"])
        if server.owner != request.user:
            raise PermissionError()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if "server_pk" in self.kwargs:
            context["owner"] = True

        return context


class IndexView(ServersMixin, TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["friends"] = services.get_friends(self.request.user)

        return context


class ServerCreateView(ServersMixin, CreateView):
    model = models.Server
    form_class = forms.ServerCreateForm
    template_name = "app/server_create.html"

    def get_success_url(self):
        return reverse_lazy("app:server-detail", kwargs={"server_pk": self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()
        services.server_default_role(self.object)
        return HttpResponseRedirect(self.get_success_url())


class ServerDetailView(ServersMixin, ServerMemberMixin, DetailView):
    model = models.Server
    template_name = "app/server_detail.html"
    pk_url_kwarg = "server_pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["role_form"] = forms.RoleForm()
        context["server_members_form"] = forms.ServerMembersForm()
        return context


class ServerJoinView(LoginRequiredMixin, FormView):
    form_class = forms.ServerJoinForm
    template_name = "app/server_join.html"
    pk_url_kwarg = "server_pk"

    def dispatch(self, request, *args, **kwargs):
        # Get decode id from url
        try:
            encoded_id = self.kwargs["invite_code"]
            server_id = services.server_id_decode(encoded_id)
            server = models.Server.objects.get(pk=server_id)
            self.object = server
        except models.Server.DoesNotExist:
            return Http404

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["object"] = self.object

        return context

    def get_initial(self):
        return {"invite_code": self.kwargs["invite_code"]}

    def form_valid(self, form):
        if self.request.user not in self.object.members.all():
            messages.success(self.request, "You have joined the server.")
            self.object.members.add(self.request.user)
        else:
            messages.success(self.request, "You are already a member.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("app:server-detail", kwargs={"server_pk": self.object.pk})


class ServerSettings(ServersMixin, ServerOwnerMixin, UpdateView):
    model = models.Server
    form_class = forms.ServerSettingsForm
    template_name = "app/serverSettings.html"
    pk_url_kwarg = "server_pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        id_encodeed = self.object.id_encoded()
        context["invite_link"] = id_encodeed
        context["site"] = self.request.get_host()

        return context


class ServerMembersUpdateView(ServersMixin, ServerOwnerMixin, UpdateView):
    model = models.Server
    form_class = forms.ServerMembersForm
    template_name = "app/server_members_update.html"
    pk_url_kwarg = "server_pk"

    def get_success_url(self):
        return reverse_lazy("app:server-members", kwargs={"server_pk": self.object.pk})

    def form_valid(self, form):
        # Use member id to remove
        member = User.objects.get(pk=form.cleaned_data["member_id"])
        self.object.members.remove(member)
        return super().form_valid(form)


class ServerUpdateView(ServersMixin, UpdateView):
    """
    This will allow for server name and icon update.
    """

    model = models.Server
    form_class = forms.ServerEditForm
    template_name = "app/server_update.html"
    pk_url_kwarg = "server_pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ServerRoleUpdateView(ServersMixin, UpdateView):
    model = models.Role
    form_class = forms.RoleForm
    template_name = "app/role_update.html"
    pk_url_kwarg = "role_pk"

    def get_success_url(self):
        return reverse_lazy(
            "app:server-detail", kwargs={"server_pk": self.object.server.pk}
        )


class CreateTextChannelView(ServersMixin, ServerOwnerMixin, CreateView):
    model = models.TextChannel
    form_class = forms.TextChannelCreateForm
    template_name = "app/textchannel_create.html"
    pk_url_kwarg = "server_pk"

    def get_success_url(self):
        return reverse_lazy(
            "app:channel-detail",
            kwargs={
                "server_pk": self.kwargs["server_pk"],
                "textchannel_pk": self.object.pk,
            },
        )

    def form_valid(self, form):
        form.instance.server = models.Server.objects.get(pk=self.kwargs["server_pk"])
        return super().form_valid(form)


class TextChannelMessageCreateView(ServersMixin, ServerMemberMixin, CreateView):
    model = models.TextChannel
    form_class = forms.TextChannelMessageForm
    template_name = "app/textchannel_detail.html"
    pk_url_kwarg = "textchannel_pk"

    def dispatch(self, request, *args, **kwargs):
        try:
            self.channel = models.TextChannel.objects.get(
                pk=self.kwargs["textchannel_pk"]
            )
        except models.TextChannel.DoesNotExist:
            return Http404
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["channel"] = self.channel

        return context

    def get_success_url(self):
        return HttpResponseRedirect(
            reverse_lazy(
                "app:channel-detail",
                kwargs={
                    "server_pk": self.kwargs["server_pk"],
                    "textchannel_pk": self.kwargs["textchannel_pk"],
                },
            )
        )

    def form_valid(self, form):
        form.instance.channel = self.channel
        form.instance.author = self.request.user
        form.save()
        return HttpResponseRedirect(
            reverse_lazy(
                "app:channel-detail",
                kwargs={
                    "server_pk": self.kwargs["server_pk"],
                    "textchannel_pk": self.kwargs["textchannel_pk"],
                },
            )
        )


class FriendRequestListView(ServersMixin, ListView):
    model = models.FriendRequest
    template_name = "app/friend_request_list.html"

    def get_queryset(self):
        return models.FriendRequest.objects.filter(
            to_user=self.request.user, accepted=False
        )


class FriendRequestUpdateView(ServersMixin, UpdateView):
    model = models.FriendRequest
    form_class = forms.FriendRequestUpdateForm
    template_name = "app/friend_request_update.html"
    success_url = reverse_lazy("app:friend-requests")
    pk_url_kwarg = "request_pk"

    def dispatch(self, request, *args, **kwargs):
        dispatch = super().dispatch(request, *args, **kwargs)
        if self.object:
            if self.object.accepted:
                messages.add_message(
                    self.request,
                    messages.ERROR,
                    "Friend request already accepted.",
                    extra_tags="danger",
                )
                return HttpResponseRedirect(reverse_lazy("app:friend-requests"))
        return dispatch

    def form_valid(self, form):
        if form.instance.accepted:
            messages.success(self.request, "Friend request accepted.")
        return super().form_valid(form)


class FriendRequestCreateView(ServersMixin, FormView):
    form_class = forms.FriendRequestCreateForm
    template_name = "app/friend_request_create.html"
    success_url = reverse_lazy("app:friend-requests")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["friendrequests"] = models.FriendRequest.objects.filter(
            to_user=self.request.user
        )
        return context

    def form_valid(self, form):
        to_user = form.cleaned_data["to_user"]
        try:
            user = User.objects.get(username=to_user)
            request_check = models.FriendRequest.objects.filter(
                by_user=self.request.user, to_user=user
            )
            if request_check.exists():
                messages.add_message(
                    self.request,
                    messages.ERROR,
                    f"Friend request already sent to {user}.",
                    extra_tags="danger",
                )
                return super().form_valid(form)
        except User.DoesNotExist:
            return self.render_to_response(self.get_context_data(form=form))

        friend_request = models.FriendRequest.objects.create(
            to_user=user, by_user=self.request.user
        )
        messages.success(self.request, f"Friend request sent to {user}.")
        return super().form_valid(form)


class DirectMessageCreateView(ServersMixin, CreateView):
    model = models.DirectMessage
    form_class = forms.DirectMessageCreateForm
    template_name = "app/direct_message_create.html"

    def dispatch(self, request, *args, **kwargs):
        try:
            self.other_user = User.objects.get(pk=self.kwargs["user_pk"])
        except User.DoesNotExist:
            return Http404

        # Check if the users are friends
        friend_check = models.FriendRequest.objects.filter(
            Q(by_user=self.request.user, to_user=self.other_user)
            | Q(by_user=self.other_user, to_user=self.request.user),
            accepted=True,
        )
        if not friend_check.exists():
            return Http404

        try:
            self.channel = models.DirectMessageChannel.objects.get(
                Q(user1=self.request.user, user2=self.other_user)
                | Q(user1=self.other_user, user2=self.request.user)
            )
        except models.DirectMessageChannel.DoesNotExist:
            # Make the direct message channel
            self.channel = models.DirectMessageChannel.objects.create(
                user1=self.request.user, user2=self.other_user
            )

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["channel"] = self.channel
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.channel = self.channel
        form.save()
        return HttpResponseRedirect(
            reverse_lazy("app:direct-message", kwargs=self.kwargs)
        )
