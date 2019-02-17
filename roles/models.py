from django.contrib.auth.models import AbstractUser
from django.core.validators import URLValidator
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (2, 'Recipient'),
        (5, 'LocalBody'),
        (6, 'Admin'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=6)
    name = models.CharField(max_length=50, default='')

class Recipient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=40, default='')
    age = models.CharField(max_length=2, default='')
    Education = (
        ('u', 'Uneducated'),
        ('sch', 'School'),
        ('ssc', 'SSC'),
        ('hsc', 'HSC'),
        ('grad', 'Graduate'),
        ('postgrad', 'Post Graduate'),
    )
    education = models.CharField(max_length=13, choices=Education, default='Uneducated')

    Designation = (
        ('Student', 'Student'),
        ('Govt_Employee', 'Govt. Employee'),
        ('Business', 'Businessman'),
        ('Private_Employee', 'Private Employee' ),
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
    gender = models.CharField(max_length=1, choices=GENDERS, default='Other')


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
    Category = (
        ('edu', 'Education'),
        ('busi', 'Business'),
        ('pension', 'Pension'),
        ('loans', 'Loans'),
        ('agri', 'Agriculture'),
        ('health', 'Healthcare'),
        ('others', 'Others'),
    )
    category = models.CharField(max_length=12, choices=Category, default='Others')
    description = models.CharField(max_length=500, default='')
    el_age = models.CharField(max_length=2, default='')
    Education = (
        ('u','Uneducated'),
        ('sch','School'),
        ('ssc','SSC'),
        ('hsc','HSC'),
        ('grad','Graduate'),
        ('postgrad','Post Graduate'),
    )
    el_education = models.CharField(max_length=13, choices=Education, default='Uneducated')

    Designation = (
        ('Student', 'Student'),
        ('Govt. Employee', 'Govt. Employee'),
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
    GENDER_NA = 'NA'
    GENDERS = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
        (GENDER_NA, 'N/A'),
    )
    el_gender = models.CharField(max_length=1, choices=GENDERS, default='N/A')
    link = models.TextField(validators=[URLValidator()], default='')
    poster = models.FileField(null=True,blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.organizer
