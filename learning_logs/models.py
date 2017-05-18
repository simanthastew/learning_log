# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Topic(models.Model):
	""" a topic the user is learning about """
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		""" return string representation of the model """
		return self.text
