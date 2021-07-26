from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets
from django.forms.forms import Form
from .models import CustomUserModel


class RegisterForm(UserCreationForm):

    #image = forms.FileField(required=False,label="Image*",widget=forms.FileInput(attrs={'class':'fields'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'fields'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'fields'}))
    
    password1 = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={'class':'passfields','style':'text-align:center; margin-left:180px; width:65%; border-radius:3px;'})
    )
    password2 = forms.CharField(
        label="Parol Tesdiqle",
        widget=forms.PasswordInput(attrs={'class':'passfields','style':'text-align:center; margin-left:180px; width:65%; border-radius:3px;'})
    )

    class Meta:
        model = CustomUserModel
        fields = ["username","email","password1","password2"]

class LoginForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'fields'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'fields'}))