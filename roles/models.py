from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

BLOOD_TYPE_CHOICES = (
    ('A+', 'A+'),
    ('B+', 'B+'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('B-', 'B-'),
    ('O-', 'O-'),
)


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Donor'),
        (2, 'Recipient'),
        (3, 'BloodBank'),
        (4, 'Hospital'),
        (5, 'LocalBody'),
        (6, 'Admin'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=6)
    name = models.CharField(max_length=50)


class Donor(models.Model):
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=40, default='')
    location = models.CharField(max_length=40, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Recipient(models.Model):
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=40, default='')
    location = models.CharField(max_length=40, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class BloodBank(models.Model):
    name = models.CharField(max_length=40, default='')
    location = models.CharField(max_length=40, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Hospital(models.Model):
    name = models.CharField(max_length=40, default='')
    location = models.CharField(max_length=40, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class LocalBodies(models.Model):
    name = models.CharField(max_length=40, default='')
    location = models.CharField(max_length=40, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class BloodDonationEvent(models.Model):
    user = models.ForeignKey(User, default=5, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    organizer = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.datetime.now())
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # time=models.TimeField()
    poster = models.FileField(null=True,blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.organizer + ' - ' + self.location


class Blood(models.Model):
    user = models.ForeignKey(User, default=6, on_delete=models.CASCADE)
    blood_type = models.CharField(choices=BLOOD_TYPE_CHOICES, default='O+', max_length=20)
    quantity = models.IntegerField()
    reports = models.FileField()
    anomaly = models.CharField(max_length=50)
    blood_bank = models.ManyToManyField(BloodBank, default=1)
    status = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, default=1)


class Request(models.Model):
    user = models.ForeignKey(User, default=6, on_delete=models.CASCADE)
    time = models.TimeField(default=datetime.datetime.now())
    request_quantity = models.IntegerField()
    request_type = models.CharField(choices=BLOOD_TYPE_CHOICES, default='O+', max_length=20)
    date = models.DateTimeField(default=datetime.datetime.now())
    location = models.CharField(default="",max_length=100)
    #description = models.CharField(default="",max_length=500)
    # time = models.TimeField()
    #poster = models.ImageField(null=True, blank=True)
    #status = models.IntegerField(default=0)
