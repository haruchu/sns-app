from django import forms
from django.contrib.auth.forms import UserCreationForm
# ユーザ作成フォームを継承
class SignUpForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
