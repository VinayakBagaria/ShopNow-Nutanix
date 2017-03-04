from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^(?P<pk>[0-9]+)/$',ProductDetailView.as_view()),
    url(r'^search/$',ProductSearchView.as_view()),
    url(r'^$',ProductListView.as_view()),
    url(r'^add_to_cart/(?P<pk>[0-9]+)/$',ProductCartView.as_view()),
]