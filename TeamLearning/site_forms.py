from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')