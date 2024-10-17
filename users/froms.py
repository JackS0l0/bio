from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
class UserLoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'forminputClass'}),label='İstifadəçi ad')
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'forminputClass'}),label='Şifrə')
    class Meta:
        model = User
        fields = ['username','password']
class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')