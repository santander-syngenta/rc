from django.db import models
from django.conf import settings
from django.template.defaultfilters import date

# Create your models here.

class FormTags(models.Model):
	name = models.CharField(max_length = 300)

	def __str__(self):
		return self.name


class Form(models.Model):
	title = models.CharField(max_length = 300, null = True)
	file = models.FileField(upload_to = "documents/", null = True)
	date = models.DateField(auto_now_add = True, null = True)
	tag = models.ManyToManyField(FormTags)

	def __str__(self):
		return self.title


class Link(models.Model):
	title = models.CharField(max_length = 300)
	url = models.CharField(max_length = 600)
	date = models.DateField(auto_now_add = True)

	def __str__(self):
		return self.title


class Subject(models.Model):
	name = models.CharField(max_length = 300)

	def __str__(self):
		return self.name


class Content(models.Model):
	title = models.CharField(max_length = 300, null = True)
	file = models.FileField(upload_to = "documents/training/", null = True)
	file2 = models.FileField(upload_to = "documents/training/", null = True, blank = True)
	date = models.DateField(auto_now_add = True, null = True)
	subject = models.ManyToManyField(Subject)

	def __str__(self):
		return self.title


class Form2(models.Model):
	title = models.CharField(max_length = 300, null = True)
	file = models.FileField(upload_to = "documents/resourceForms/", null = True)
	date = models.DateField(auto_now_add = True, null = True)

	def __str__(self):
		return self.title
	

class Contact(models.Model):
	email = models.CharField(max_length = 300, null = True)
	name = models.CharField(max_length = 300, null = True)
	number = models.CharField(max_length = 300, null = True)
	speciality = models.TextField(max_length = 300, null = True)

	def __str__(self):
		return self.name

