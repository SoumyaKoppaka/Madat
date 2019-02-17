import django_filters
from roles.models import BloodDonationEvent
class UserFilter(django_filters.FilterSet):
    class Meta:
        model = BloodDonationEvent
        fields = ['category']