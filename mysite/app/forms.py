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
        fields = ["members"]

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


class TextChannelMessageForm(forms.ModelForm):
    class Meta:
        model = models.TextChannelMessage
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
