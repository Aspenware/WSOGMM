from django.db import models

class School(models.Model):
	name = models.CharField(max_length=128)

def __str__(self):
	return self.name

class Account(models.Model):
# id is done automagically
	username = models.CharField(max_length=128)
	password = models.CharField(max_length=256)
	email = models.CharField(max_length=256)
	realname = models.CharField(max_length=256)
	priviledge = models.IntegerField(default=1)
	is_confirmed = models.BooleanField(default=False)
	confirmation_code = models.CharField(max_length=128)
	school = models.ForeignKey(School)
	def __str__(self):
		return self.username 