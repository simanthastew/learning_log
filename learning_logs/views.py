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
	topics = Topics.objects.order_by('date_added')
	context = {'topics': topics}
	#context is a dictionary sent to the template where keys are names used in the template to access data
	return render(request, 'learning_logs/topics.html', context)
	#if you want context to be available, have to pass it to render function