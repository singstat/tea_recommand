from django import forms
from django.forms import Textarea

from .models import Entry, Company

class PostForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('tea_info','like','comment')
        widgets = {
                    'comment': Textarea(attrs={'cols': 100, 'rows': 1}),
                }

class TeaInfo(forms.Form):
	company_name = forms.CharField()
	tea_name = forms.CharField(max_length = 100)