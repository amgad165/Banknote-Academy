from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username','first_name', 'last_name','email','password1','password2','phone_number','Academic_Year','College','University')

class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username','first_name', 'last_name','email','phone_number','Academic_Year','College','University')
