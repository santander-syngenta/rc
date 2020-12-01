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


class Link(models.Model):
	title = models.CharField(max_length = 300)
	url = models.CharField(max_length = 600)
	date = models.DateField(auto_now_add = True)

	def __str__(self):
		return self.title


class Content(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, null=True, on_delete = models.SET_NULL)
    name = models.CharField(max_length=120, null=True, blank=True)
    path = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(default=0)
    file_type = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    @property
    def title(self):
        return str(self.name)