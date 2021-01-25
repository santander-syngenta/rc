from django.db import models

# Create your models here.

class Question(models.Model):
	txt = models.TextField()
	asked = models.DateTimeField(auto_now_add = True)


class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	answer = models.TextField()
	answered = models.DateTimeField(auto_now_add = True)


class Announcement(models.Model):
	headline = models.TextField()
	body = models.TextField(null = True)
	link = models.CharField(max_length = 200, null = True, blank = True)

	