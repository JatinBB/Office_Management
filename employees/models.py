from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.fname} {self.lname}'
# # Example of creating roles
#     admin_group, created = Group.objects.get_or_create(name='Admin')
#     manager_group, created = Group.objects.get_or_create(name='Manager')