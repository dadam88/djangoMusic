from django import forms
from django.forms import ModelForm
from django.template.defaultfilters import slugify

from piano.models import Composer, Song
import itertools

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
        fields = ['name', 'level', 'composer', 'period']

        def __unicode__(self):
            return self.name

    def save(self):
        # Unique slug code from
        # https://keyerror.com/blog/automatically-generating-unique-slugs-in-django
        instance = super(SubmitAWork, self).save(commit=False)

        max_length = Song._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.name)[:max_length]

        for x in itertools.count(1):
            if not Song.objects.filter(slug=instance.slug).exists():
                break

            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        instance.save()

        return instance

