from django.contrib.auth.forms import UserCreationForm #From ModelForms, we imported UserCreationForm 
from django.contrib.auth.models import User #From built-in models, we imported User model(contains default fields like username, password, first name, second name, email etc)
from django import forms

class UserRegistration(UserCreationForm): #created this class to tweak UserCreationForm
	class Meta:
		model=User #Our blueprint model 
		fields=['username','first_name', 'email','password1','password2'] #username and email are fields of User model and password1 and password2 are fields created in UserCreationForm i.e. password1 for create password and password2 for confirm password
