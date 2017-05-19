from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}
		#tells django not to generate a label for the text field