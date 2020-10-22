from django.db import models
from django.conf import settings

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