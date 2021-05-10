from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from HallBooking.models import Updf
from django.forms import ModelForm

class Usrg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["username","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Email id",
			}),
		}

class UpdaPfl(ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update First Name"
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Last Name"
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Emailid"
			}),
		}

class Im(ModelForm):
	class Meta:
		model = Updf
		fields = ["age","gender","im"]
		widgets = {
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			}),
		}

