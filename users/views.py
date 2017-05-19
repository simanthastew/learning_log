# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django contribauth import logout

def logout_view(request):
	#called logout_view so we can call django logout funciton later
	""" log the user out """
	logout(request)
	#logout function is imported from django and does not need to be created
	return HttpResponseRedirect(reverse('learning_logs:index'))
