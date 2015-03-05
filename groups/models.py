from django.db import models
from users.models import User


# Create your models here.
class Group(models.Model):
    name = models.CharField()
    owner = models.ForeignKey(User)
    # Parent references my parent group, if I have one
    parent = models.ForeignKey("self", null=True, blank=True)
    access_code = models.CharField()
    expiration_date = models.DateTimeField()
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, null=True)
    modified_at = models.DateTimeField()


class Enrollment(models.Model):
    group = models.ForeignKey(Group)
    user = models.ForeignKey(User)
