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
    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)
    class meta (): 
        verbose_name= "Doctor"
        verbose_name_plural= "Doctors"
    def __str__(self):
        return f"Dr.{self.first_name} {self.last_name}"   

class Patient (User):
    national_id = models.CharField(max_length=8,unique=True,validators=[number_validator])
    phone = models.CharField(max_length=8,unique=True,validators=[number_validator])
    birth_date = models.DateField(validators=[birth_date_validator])
    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)
    class meta ():
        verbose_name= "Patient"
        verbose_name_plural= "Patients"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"   

class Specialty (models.Model):
    name = models.CharField(max_length=50, blank=False) 
    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)
    class meta ():
        verbose_name= "Specialty"
        verbose_name_plural= "Specialtys" 

    def __str__(self):
        return self.name    


