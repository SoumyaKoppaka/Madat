from django.contrib import admin
from django.urls import path, include
from roles.views import all_roles, recipients, local_bodies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('roles.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', all_roles.SignUpView.as_view(), name='signup'),
    #path('accounts/signup/donor/', donors.DonorSignUpView.as_view(), name='donor_signup'),
    path('accounts/signup/recipient/', recipients.RecipientSignUpView.as_view(), name='recipient_signup'),
    #path('accounts/signup/hospital/', hospitals.HospitalSignUpView.as_view(), name='hospital_signup'),
    #path('accounts/signup/bloodBank/', blood_banks.BloodBankSignUpView.as_view(), name='blood_bank_signup'),
    path('accounts/signup/localBody/', local_bodies.LocalBodySignUpView.as_view(), name='local_bodies_signup'),
    path('viewEvents/', local_bodies.view_event, name='view_events'),
    path('about/', all_roles.about, name='about'),
    path('contact/', all_roles.contact, name='contact'),
]
