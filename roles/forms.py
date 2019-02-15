from django import forms
from django.contrib.auth.forms import UserCreationForm
from roles.models import User, Recipient, LocalBodies, BloodDonationEvent

class RecipientSignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput,
        required=True
    )

    last_name = forms.CharField(
        widget=forms.TextInput,
        required=True
    )

    location = forms.CharField(
        widget=forms.TextInput,
        required=True,
    )

    email_address = forms.EmailField(
        widget=forms.TextInput,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2
        user.email = self.cleaned_data.get('email_address')
        user.save()
        recipient = Recipient.objects.create(user=user)
        recipient.first_name = self.cleaned_data.get('first_name')
        recipient.last_name = self.cleaned_data.get('last_name')
        recipient.location = self.cleaned_data.get('location')
        recipient.save()
        return user


class LocalBodySignUpForm(UserCreationForm):
    name = forms.CharField(
        widget=forms.TextInput,
        required=True
    )

    location = forms.CharField(
        widget=forms.TextInput,
        required=True,
    )

    email_address = forms.EmailField(
        widget=forms.TextInput,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 5
        user.email = self.cleaned_data.get('email_address')
        user.save()
        local_body = LocalBodies.objects.create(user=user)
        local_body.save()
        return user

class EventForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput,
        required=True
    )

    description = forms.CharField(
        widget=forms.Textarea,
        required=True
    )

    class Meta:
        model = BloodDonationEvent
        fields = ['name', 'organizer', 'location', 'date', 'description']