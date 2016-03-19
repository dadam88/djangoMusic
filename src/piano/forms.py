from django import forms
from django.forms import ModelForm

from piano.models import Composer, Song

class SearchForm(forms.Form):
   search_term = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))


class AdvancedSearchForm(forms.Form):
	c = Composer.objects.all()
	p = ['Baroque', 'Classical','Romantic','Modern']

	levels = forms.ChoiceField(choices=[('null', '')] + [(x, x) for x in range(1, 11)])
	composers = forms.ChoiceField(choices=[('null', '')] + [(comp, comp) for comp in c])
	periods = forms.ChoiceField(choices=[('null', '')] + [(per, per) for per in p])

class SubmitAWork(ModelForm):
	class Meta:
		model = Song
		fields = ['name', 'level', 'composer', 'period', 'slug']

		def __unicode__(self):
			return self.name
