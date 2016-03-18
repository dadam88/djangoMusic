from django import forms

from .models import SearchBar

class SearchBarForm(forms.ModelForm):
	class Meta:
		model = SearchBar