from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^Catalogo/$',views.CatalogoListView.as_view(),name="catalogo_list"),
	url(r'^Catalogo/(?P<pk>\d+)/$',views.CatalogoDetailView.as_view(),name="catalogo_detail"),
]