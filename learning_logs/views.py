# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
	""" home page for learning log """
	return render(request, 'learning_logs/index.html')