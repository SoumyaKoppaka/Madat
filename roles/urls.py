from django.urls import include, path
from .views import all_roles, recipients, local_bodies
from django.conf.urls import url

urlpatterns = [

    path('', all_roles.home, name='home'),

    path('recipient/', include(([
                                    path('', recipients.RecipientHomeView.as_view(), name='recipient_home'),
                                ], 'roles'), namespace='recipient')),

    path('localBodies/', include(([
                                      path('', local_bodies.LocalBodyHomeView.as_view(), name='local_bodies_home'),
                                      path('uploadEvents', local_bodies.upload_event, name='upload_events'),
                                  ], 'roles'), namespace='local_bodies')),

]
