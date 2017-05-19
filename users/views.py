# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
#above are all preset django functions that you can call after you import them
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
	#called logout_view so we can call django logout funciton later
	""" log the user out """
	logout(request)
	#logout function is imported from django and does not need to be created
	return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
	""" register new user """
	if request.method != 'POST':
		#display blank registration form
		form = UserCreationForm()
	else:
		#process complete, making post request to register new user
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			#log user in and redirect to home page
			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
			#user asked to enter two passwords, since form is valid, passwords match and we can get the password from the value associated with the password1 key in the form's post data
			login(request, authenticated_user)
			#if user is authenticated, call login function on authenticated_user
			return HttpResponseRedirect(reverse('learning_logs:index'))

	context = {'form': form}
	return render(request, 'users/register.html', context)

