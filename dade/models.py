from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
	user = models.OneToOneField(User)
	realname = models.CharField(max_length=256)
	priviledge = models.IntegerField(default=1)
	is_confirmed = models.BooleanField(default=False)
	confirmation_code = models.CharField(max_length=128)
	accountschool = models.ForeignKey("School")
	def __str__(self):
		return self.username
class Group(models.Model):
	name = models.CharField(max_length=128)
	groupschool = models.ForeignKey("School")
	accounts = models.ManyToManyField(Account, verbose_name="Accounts")
class School(models.Model):
	name = models.CharField(max_length=128)
	schoolaccounts = models.ManyToManyField(Account, verbose_name="Accounts")
	groups = models.ManyToManyField(Group, verbose_name="Groups")
	def __str__(self):
		return self.name
class Assignment(models.Model):
	name = models.CharField(max_length=128)
	school = models.ForeignKey(School)
	group = models.ForeignKey(Group)
class Notification(models.Model):
	notifytype = models.CharField(max, max_length=128)
