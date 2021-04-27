from django import forms
# from django.forms import ModelForms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

 
class ResgisterForm(UserCreationForm):
    email = forms.EmailField(max_length = 200, required=True, label='Email')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        labels = {'email': 'Email ID',}