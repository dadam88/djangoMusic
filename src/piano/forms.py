from django import forms

from piano.models import Composer, Song
class SearchForm(forms.Form):
   search_term = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))


class AdvancedSearchForm(forms.Form):
	c = Composer.objects.all()
	p = ['Baroque', 'Classical','Romantic','Modern']

	levels = forms.ChoiceField(choices=[(x, x) for x in range(1, 11)])
	
	composers = forms.ChoiceField(choices=[(comp, comp) for comp in c])
	period = forms.ChoiceField(choices=[(per, per) for per in p])

