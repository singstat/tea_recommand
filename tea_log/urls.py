from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.tea_list,name='tea_list'),
    url(r'^(?P<un>\w+)/$', views.user_detail, name='user_detail'),
    url(r'^/new/$', views.add_new, name='add_new'),
	url(r'^/new_tea/$', views.add_tea, name='add_tea')
]