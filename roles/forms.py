from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import URLValidator
from roles.models import User, Recipient, LocalBodies, BloodDonationEvent

class RecipientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    age = forms.CharField(required = True)
    gender = forms.ChoiceField(choices=Recipient.GENDERS, required=True)
    designation = forms.ChoiceField(choices=Recipient.Designation ,required=True)
    education = forms.ChoiceField(choices=Recipient.Education, required=True)
    income = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2
        #user.email = self.cleaned_data.get('email_address')
        user.save()
        recipient = Recipient.objects.create(user=user)
        recipient.first_name = self.cleaned_data.get('first_name')
        recipient.last_name = self.cleaned_data.get('last_name')
        recipient.age = self.cleaned_data.get('age')
        recipient.education=self.cleaned_data.get('education')
        recipient.gender=self.cleaned_data.get('gender')
        recipient.designation=self.cleaned_data.get('designation')
        recipient.save()
        return user


class LocalBodySignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    location = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    contact = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 5
        user.email = self.cleaned_data.get('email_address')
        user.save()
        local_body = LocalBodies.objects.create(user=user)
        local_body.name=self.cleaned_data.get('name')
        local_body.location=self.cleaned_data.get('location')
        local_body.email_address=self.cleaned_data.get('email')
        local_body.contact=self.cleaned_data.get('contact')
        local_body.save()
        return user

class EventForm(forms.ModelForm):
    name = forms.CharField(required=True)
    organizer = forms.CharField(required=True)
    contact = forms.CharField(required=True)
    description = forms.CharField(required=True)
    el_age = forms.CharField(required=False)
    el_designation = forms.ChoiceField(choices=BloodDonationEvent.Designation, required=True)
    el_education = forms.ChoiceField(choices=BloodDonationEvent.Education, required=True)
    el_income = forms.IntegerField(required=False)
    el_gender = forms.ChoiceField(choices=BloodDonationEvent.GENDERS, required=False)
    link = forms.URLField()
    poster = forms.FileField(required=False)

    class Meta:
        model = BloodDonationEvent
        fields = ['name', 'organizer','contact','description','el_age','el_designation','el_education','el_income','el_gender','link','poster']