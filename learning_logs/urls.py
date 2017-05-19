""" Defines URL patterns for learning_logs """

from django.conf.urls import url

from . import views 

urlpatterns = [
	#Home page
	url(r'^$', views.index, name='index'),
	#url function takes three arguments, regex matching url, 
	# which view function to call,
	# name for URL pattern so you can refer to it later on

	url(r'^topics/$', views.topics, name='topics'),
	#show topics^
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	#show individual topic^
	url(r'^new_topic/$', views.new_topic, name='new_topic'),
	#new topic page^
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	#new entry for specific topic ^
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
	#edit entry already saved in database^

]