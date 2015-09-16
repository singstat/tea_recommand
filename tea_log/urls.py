from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.tea_list, name='tea_list'),
]