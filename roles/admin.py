from django.contrib import admin
from .models import BloodDonationEvent,User,Recipient,LocalBodies

# Register your models here.
admin.site.register(User)
admin.site.register(Recipient)
admin.site.register(LocalBodies)
admin.site.register(BloodDonationEvent)
