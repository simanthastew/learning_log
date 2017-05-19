""" Defines URL patterns for users """

from django.conf.urls import url
from django.contrib.auth.views import login 

from . import views 

urlpatterns = [
	#login page - different from other urls because it's a default django template
	url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
] 