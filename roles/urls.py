from django.urls import include, path
from .views import donors, all_roles, recipients, hospitals, blood_banks, local_bodies
from django.conf.urls import url


urlpatterns = [

    path('', all_roles.home, name='home'),

    path('donor/', include(([
                                path('', donors.DonorHomeView.as_view(), name='donor_home'),
                                path('donate_blood', donors.donate_blood, name='donate_blood'),
                            ], 'roles'), namespace='donor')),

    path('recipient/', include(([
                                    path('', recipients.RecipientHomeView.as_view(), name='recipient_home'),
                                ], 'roles'), namespace='recipient')),

    path('bloodBank/', include(([
                                    path('', blood_banks.BloodBankHomeView.as_view(), name='blood_bank_home'),
                                ], 'roles'), namespace='blood_bank')),

    path('hospital/', include(([
                                   path('', donors.DonorHomeView.as_view(), name='hospital_home'),
                                   path('reserveBlood', hospitals.reserve_blood, name='hospital_reserve_blood'),
                                   path('search', hospitals.search, name='hospital_search'),

                                   url(r'^search/(?P<slug>[^\/]+)$', hospitals.block_blood,
                                       name='hospital_block_blood'),
                                    url(r'^sendEmailRequest/$', hospitals.send_email_request,
                                       name='hospital_send_email_request'),


                               ], 'roles'), namespace='hospital')),

    path('localBodies/', include(([
                                      path('', local_bodies.LocalBodyHomeView.as_view(), name='local_bodies_home'),
                                      path('uploadEvents', local_bodies.upload_event, name='upload_events'),
                                  ], 'roles'), namespace='local_bodies')),

]
