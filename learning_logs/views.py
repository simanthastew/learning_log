# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
#need line 5 to reference database models
from .forms import TopicForm

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

def new_topic(request):
	""" add new topic """
	if request.method != 'POST':
		form = TopicForm()
		#for get request, return blank form
		#gave no arguments, so django creates blank form
	else:
		#post data submitted
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
			#if form is saved, redirect back to topics page

	context = {'form': form}
	#the context is a form regardless of get/post, so a blank form or the filled out form is the context, but on post request you get redirected
	return render(request, 'learning_logs/new_topic.html', context)
















