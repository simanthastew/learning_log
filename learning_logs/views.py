# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic, Entry
#need line 5 to reference database models
from .forms import TopicForm, EntryForm

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
		#WHY IS THIS NOT data=request.POST ?
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
			#if form is saved, redirect back to topics page

	context = {'form': form}
	#the context is a form regardless of get/post, so a blank form or the filled out form is the context, but on post request you get redirected
	return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
	""" add a new entry for an individual topic """
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		#no data, blank form
		form = EntryForm()
	else:
		#post data submitted
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			#commit=False creates new object without saving it to the database yet since we haven't assigned it a topic id
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
			#the reverse call takes two arguments, the name of the URL and args list containing any arguments that need to be included in the url, i.e. new_entry/id

	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
	""" edit entry already saved in database """
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if request.method != 'POST':
		form = EntryForm(instance=entry)
		#prefill form with current entry, which we found off of entry id
	else:
		form = EntryForm(instance=entry, data=request.POST)
		#use instance and data args to create form instancebased on the info associated with the existing entry ojbect, updated with and relevant data from request.POST
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)
















