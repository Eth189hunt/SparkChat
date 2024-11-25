from crispy_forms.helper import FormHelper
from django import forms

from . import models


class ServerCreateForm(forms.ModelForm):
    class Meta:
        model = models.Server
        fields = ["name", "icon"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class ServerEditForm(forms.ModelForm):
    class Meta:
        model = models.Server
        fields = ["name", "icon"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class ServerMembersForm(forms.ModelForm):
    class Meta:
        model = models.Server
        fields = []

    member_id = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class RoleForm(forms.ModelForm):
    class Meta:
        model = models.Role
        exclude = ["server"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class DirectMessageCreateForm(forms.ModelForm):
    class Meta:
        model = models.DirectMessage
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].label = ""
        self.helper = FormHelper()
        self.helper.form_tag = False


class TextChannelMessageForm(forms.ModelForm):
    class Meta:
        model = models.TextChannelMessage
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].label = ""
        self.helper = FormHelper()
        self.helper.form_tag = False


class TextChannelCreateForm(forms.ModelForm):
    class Meta:
        model = models.TextChannel
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class FriendRequestCreateForm(forms.Form):
    to_user = forms.CharField(
        max_length=255,
        label="Friend Username",
        help_text="Enter the username of the user you want to friend.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class FriendRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = models.FriendRequest
        fields = ["accepted"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class ServerJoinForm(forms.Form):
    invite_code = forms.CharField(
        max_length=255,
        label="Invite Code",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["invite_code"].label = ""
        self.helper = FormHelper()
        self.helper.form_tag = False


class ServerSettingsForm(forms.ModelForm):
    class Meta:
        model = models.Server
        fields = ["name", "icon"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
