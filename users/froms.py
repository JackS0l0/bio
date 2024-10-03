from django import forms
from django.contrib.auth.forms import AuthenticationForm
class UserLoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'forminputClass'}),label='İstifadəçi ad')
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'forminputClass'}),label='Şifrə')
    class Meta:
        model = forms
        fields = ['username','password']