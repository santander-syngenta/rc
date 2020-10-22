from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms


class upload(ModelForm):
	class Meta:
		model = Form
		fields = '__all__'
		exclude = ['date']