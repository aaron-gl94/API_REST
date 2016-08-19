from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from main.api import urls as api_urls
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(),name="home"),
    url(r'^api/',include(api_urls)),
]
