from django import forms
# from django.forms import ModelForms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

 
class ResgisterForm(UserCreationForm):
    email = forms.EmailField(max_length = 200, required=False, label='Email ID')
    phone = forms.IntegerField(required=False, label='Phone No.')
    city = forms.CharField(max_length=50, required=False, label='City Name')
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'city', 'password1', 'password2', )
        # labels = {'email':'Email ID', 'city':'City Name', 'phone':'phone',}