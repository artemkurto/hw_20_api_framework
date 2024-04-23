# Create your models here.
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator, EmailValidator
from django.db import models
import re


class User(models.Model):
    username = models.CharField(max_length=10, validators=[MaxLengthValidator(10), MinLengthValidator(3)], unique=True)
    password = models.CharField(
        max_length=100,
        validators=[RegexValidator(re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,12}$'),
                                   'Min len is 6, max is 12. Al least 1 capital, 1 small, 1 number')])
    email = models.CharField(max_length=100, validators=[EmailValidator()])

    def __str__(self):
        return self.username


class JobPosition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserJobPosition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} - {self.job_position.name}"
