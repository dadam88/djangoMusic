from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe


class SearchForm(forms.Form):
	
	q = forms.CharField(widget=forms.TextInput(attrs={'id':'ajaxsearch', 'class':'ajaxsearchmain', 'placeholder':'Search articles and users'}), required=False)
