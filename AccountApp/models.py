from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
number_validator = RegexValidator(regex=r'^\d{8}$', message="doit contenir exactement8 chiffres ") 

def birth_date_validator(date):
    if date>= timezone.localdate():
        raise ValidationError("la date doit etre anterieur a la date d'aujouhdui")

class User (AbstractUser):
    pass

class Doctor (User):
    license_number = models.CharField(max_length=6, unique=True, blank=False, validators=[MinLengthValidator])
    phone = models.CharField(max_length=8,unique=True, validators=[number_validator])
    specialities= models.ManyToManyField('AccountApp.Specialty', related_name="DoctorList")

class Patient (User):
    national_id = models.CharField(max_length=8,unique=True,validators=[number_validator])
    phone = models.CharField(max_length=8,unique=True,validators=[number_validator])
    birth_date = models.DateField(validators=[birth_date_validator])

class Specialty (models.Model):
    name = models.CharField(max_length=50, blank=False)  


