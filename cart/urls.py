from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^$',CartView.as_view()),
]