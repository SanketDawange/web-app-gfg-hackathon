from django.db import models
from django.contrib.auth.models import AbstractUser
from accountsection import settings


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    status = models.IntegerField(default=0)