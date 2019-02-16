from django.contrib.auth.models import AbstractUser
#from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import URLValidator
from django.db import models
import datetime

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (2, 'Recipient'),
        (5, 'LocalBody'),
        (6, 'Admin'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=6)
    name = models.CharField(max_length=50, default='')

class Recipient(models.Model):
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=40, default='')
    #location = models.CharField(max_length=40, default='')

    age = models.CharField(max_length=2, default='')

    Education = (
        ('Uneducated', 'u'),
        ('School', 'sch'),
        ('SSC', 'ssc'),
        ('HSC', 'hsc'),
        ('Graduate', 'grad'),
        ('Post Graduate', 'postgrad'),
    )
    education = models.CharField(max_length=13, choices=Education, default='Uneducated')

    Designation = (
        ('Govt. Employee', 'Govt_Employee'),
        ('Businessman', 'Business'),
        ('Private Employee', 'Private_Employee'),
        ('Unemployed', 'Unemployed'),
        ('Others', 'Others'),
    )
    designation = models.CharField(max_length=16, choices=Designation, default='Others')
    income = models.IntegerField(default=0)
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'
    GENDERS = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS, default='O')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class LocalBodies(models.Model):
    name = models.CharField(max_length=40, default='')
    location = models.CharField(max_length=40, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact = models.CharField(max_length=10, default='')
    email = models.EmailField(default='')
    def __str__(self):
        return self.user.username


class BloodDonationEvent(models.Model):
    user = models.ForeignKey(User, default=5, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='')
    organizer = models.CharField(max_length=50, default='')
    contact = models.CharField(max_length=10,default='')
    description = models.CharField(max_length=500, default='')
    el_age = models.CharField(max_length=2, default='')
    Education = (
        ('Uneducated', 'u'),
        ('School', 'sch'),
        ('SSC', 'ssc'),
        ('HSC', 'hsc'),
        ('Graduate', 'grad'),
        ('Post Graduate', 'postgrad'),
    )
    el_education = models.CharField(max_length=13, choices=Education, default='Uneducated')

    Designation = (
        ('Govt. Employee', 'Govt_Employee'),
        ('Businessman', 'Business'),
        ('Private Employee', 'Private_Employee'),
        ('Unemployed', 'Unemployed'),
        ('Others', 'Others'),
    )
    el_designation = models.CharField(max_length=16, choices=Designation, default='Others')
    el_income = models.IntegerField(default=0)
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'
    GENDERS = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
    )
    el_gender = models.CharField(max_length=1, choices=GENDERS, default='O')
    link = models.TextField(validators=[URLValidator()], default='')
    poster = models.FileField(null=True,blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.organizer + ' - ' + self.location
