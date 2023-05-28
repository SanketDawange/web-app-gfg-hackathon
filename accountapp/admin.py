from django.contrib import admin
from .models import Category, Hospital, Appointment, CustomUser
# Register your models here.

Models = [Category, Hospital, Appointment, CustomUser]
for model in Models:
    admin.site.register(model)