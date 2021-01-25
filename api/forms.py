from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms


class upload(ModelForm):
	class Meta:
		model = Form
		fields = '__all__'
		exclude = ['date']


class uploadTrainingContent(ModelForm):
	class Meta:
		model = Content
		fields = '__all__'
		exclude = ['date']


class uploadResourceForm(ModelForm):
	class Meta:
		model = Form2
		fields = '__all__'
		exclude = ['date']