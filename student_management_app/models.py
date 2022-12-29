from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    HOD = '1'
    STAFF = '2'
    STUDENT = '3'

    EMAIL_TO_USER_TYPE_MAP = {
        'hod': HOD,
        'staff': STAFF,
        'student': STUDENT
    }

    user_type_data = ((HOD, "HOD"), (STAFF, "Staff"), (STUDENT, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class Staffs(models.Model):
    name = models.CharField


class AdminHOD(models.Model):
    name = models.CharField


class Students(models.Model):
    name = models.CharField
