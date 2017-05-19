# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Topic
#need line 5 to reference database models

def index(request):
	""" home page for learning log """
	return render(request, 'learning_logs/index.html')

def topics(request):
	""" show all topics """
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	#context is a dictionary sent to the template where keys are names used in the template to access data
	return render(request, 'learning_logs/topics.html', context)
	#if you want context to be available, have to pass it to render function

def topic(request, topic_id):
	""" show individual topic with its entries """
	topic = Topic.objects.get(id=topic_id)
	#topic_id will be pulled from url
	entries = topic.entry_set.order_by('-date_added')
	#dash before date_added sorts entries in reverse order
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)