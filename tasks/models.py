# Create your models here.
from django.db import models

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=20000)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class User(models.Model):
	username= models.CharField('User Name', max_length=100)
	email= models.CharField('User email', max_length=100)
	password= models.CharField('User password', max_length=100)
	def __str__(self):
		return self.username