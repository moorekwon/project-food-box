from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SigninForm(forms.ModelForm):
    class Meta:
        model = User
