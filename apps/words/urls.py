from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^words/', views.index),
	url(r'^new_word', views.new_word),
	url(r'^clear', views.clear)
]