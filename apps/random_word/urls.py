from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^random_word/$', views.index),
	url(r'^random$', views.random),
]