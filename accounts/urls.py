from django.conf.urls import url
from .views import *


urlpatterns=[
    url(r'^registration',UserRegistrationView.as_view(),name='register')
]