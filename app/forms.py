from django import forms
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class SignUpForm(UserCreationForm):
	firstName = forms.CharField()
	lastName = forms.CharField()
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('firstName','lastName','username','email', 'password1', 'password2')
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['firstName'].widget.attrs['placeholder'] = "Имя"
		self.fields['lastName'].widget.attrs['placeholder'] = "Фамилия"
		self.fields['username'].widget.attrs['placeholder'] = "Имя пользователя"
		self.fields['email'].widget.attrs['placeholder'] = "E-mail"
		self.fields['password1'].widget.attrs['placeholder'] = "Пароль"
		self.fields['password2'].widget.attrs['placeholder'] = "Повторить пароль"


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','password')