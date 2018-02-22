from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^amadon/$', views.index),
	url(r'^checkout/$', views.checkout),
	url(r'^buy$', views.buy)
]