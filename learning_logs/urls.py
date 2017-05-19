""" Defines URL patterns for learning_logs """

from django.conf.urls import url

from . import views 

urlpatterns = [
	#Home page
	url(r'^$', views.index, name='index'),
	#url function takes three arguments, regex matching url, 
	# which view function to call,
	# name for URL pattern so you can refer to it later on

	#show topics
	url(r'^topics/$', views.topics, name='topics'),
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]