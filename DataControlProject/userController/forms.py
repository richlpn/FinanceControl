from django import forms
from .models import user_login_Model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserLogin_forms(forms.ModelForm):
    username = forms.CharField(max_length=50,
                               required=True,
                               error_messages={
                                   'required': 'Enter a valid username'},
                               widget=forms.TextInput(attrs={
                                   'id': 'username',
                                   'class': 'form-control'}
                               )
                               )
    password = forms.CharField(max_length=25,
                               required=True,
                               error_messages={
                                   'required': 'Enter a valid Password'},
                               widget=forms.PasswordInput(attrs={
                                   'id': 'password',
                                   'class': 'form-control'}
                               )
                               )

    class Meta:
        model = user_login_Model
        fields = [
            'username',
            'password',
        ]


class UserCreate_forms(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
