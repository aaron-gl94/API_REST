from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(),name="home"),
]
