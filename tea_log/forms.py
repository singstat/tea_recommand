from django import forms
from django.forms import Textarea

from .models import Entry, Company, TeaName, Tea

from django.forms import ModelChoiceField

class PostForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('tea_info','like','comment')
        widgets = {
                    'comment': Textarea(attrs={'cols': 100, 'rows': 1}),
                }

class TeaInfo(forms.Form):
	company_name = forms.CharField(max_length = 100)
	tea_name     = forms.CharField(max_length = 100)
	#company_choice = forms.ModelChoiceField(queryset = Company.objects.all(), required = False)
	#tea_choice     = forms.ModelChoiceField(queryset = TeaName.objects.all(), required = False)
	#nation         = 
	#region         =
	#status         =
	def save(self):
		data = self.cleaned_data
		Company.objects.create(name = data['company_name'])
		TeaName.objects.create(name = data['tea_name'])
	

class TeaForm(forms.ModelForm):
    class Meta:
        model = Tea
        fields = ('name','company','nation','region','color','status')

#class get_input(forms.Form):
        