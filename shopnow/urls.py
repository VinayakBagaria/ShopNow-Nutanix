"""shopnow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from products.views import *

urlpatterns = [
    url(r'^$',ProductListView.as_view(),name='home'),
    url(r'^admin/',admin.site.urls),
    url(r'^products/',include('products.urls')),
    url(r'^cart/',include('cart.urls')),
    url(r'^search$',ProductSearchView.as_view(),name='search'),
    url(r'^accounts/',include('accounts.urls')),
    url('^', include('django.contrib.auth.urls'))
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
    authentication views : includes
    ^login/$ [name='login']
    ^logout/$ [name='logout']
    ^password_change/$ [name='password_change']
    ^password_change/done/$ [name='password_change_done']
    ^password_reset/$ [name='password_reset']
    ^password_reset/done/$ [name='password_reset_done']
    ^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
    ^reset/done/$ [name='password_reset_complete']
"""
