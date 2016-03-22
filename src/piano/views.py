from django.shortcuts import render

from .models import Song, Composer, Book
from .forms import SearchForm, AdvancedSearchForm, SubmitAWork
from django.db.models import Q
from django.template.defaultfilters import slugify

# Create your views here.
def all_songs(request):
    songs = Song.objects.all().order_by('name')
    field_names = Song._meta.get_all_field_names()
    context = { 'songs': songs,
                'search_bar': SearchForm(),
                'field_names': field_names,
     }
    
    # Passes variables to home.html through context list of variables
    return render(request, "songsall.html", context)

def single_song(request, songslug):
    song = Song.objects.get(slug=songslug)
    context = { 'song': song,
                'search_bar': SearchForm(),
                 }
    return render(request, "singlesong.html", context)


def composer_page(request, composerslug):
    composer = Composer.objects.get(slug=composerslug)
    composer_songs = Song.objects.all().filter(composer__slug=composerslug)
    context = { 'composer': composer, 'composer_songs': composer_songs,
                'search_bar': SearchForm(),
                 }
    return render(request, "composer.html", context)

def single_book(request, bookslug):
    book = Book.objects.get(slug=bookslug)
    
    context = { 'book': book,
                'search_bar': SearchForm(),
                 }
    return render(request, "singlebook.html", context)


def newview(request):
    context = {'search_bar': SearchForm(),
                    'submitawork': SubmitAWork()
        }
    
    if request.method == 'POST':

        form = SubmitAWork(request.POST)

        if form.is_valid():

            form.save()
    else:
        pass

    return render(request, "newview.html", context)

def home(request):
   
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():


            search_term = form.cleaned_data.get('search_term')
            
            songlist = Song.objects.filter(Q(name__icontains=search_term) | Q(composer__name__icontains=search_term))
            composerlist = Composer.objects.filter(name__icontains=search_term)
            results = []
            results = list(songlist) + list(composerlist)
            # for song in songlist:
            #   results.append(song)

            # for composer in composerlist:
            #   results.append(composer)

            # for result in results:
            #   print result
            context = {
                    'composerlist': composerlist,
                    'songlist': songlist,
                    'search_bar': SearchForm(),
            }

            return render(request, 'results_of_search.html', context)
            # return render(request, 'results_of_search.html', {'results': results})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
        
    return render(request, 'home.html', {'search_bar': form})

def advanced_search(request):
    

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AdvancedSearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            currentlist = Song.objects.all()
            composerlist = Composer.objects.all()

            if form.cleaned_data.get('levels') != 'null':
                currentlist = currentlist.filter(level=form.cleaned_data.get('levels'))
            if form.cleaned_data.get('periods') != 'null':
                currentlist = currentlist.filter(period=form.cleaned_data.get('periods'))
            if form.cleaned_data.get('composers') != 'null':
                currentlist = currentlist.filter(composer__name=form.cleaned_data.get('composers'))
                composerlist = composerlist.filter(name=form.cleaned_data.get('composers'))

            songlist = currentlist
            print currentlist

            context = { 'advanced_search': AdvancedSearchForm(),
                'search_bar': SearchForm(), 
                'songlist': songlist,
                'composerlist': composerlist,
                
                }

            return render(request, 'results_of_search.html', context)
            # return render(request, 'results_of_search.html', {'results': results})


    # if a GET (or any other method) we'll create a blank form
    else:
        context = { 'advanced_search': AdvancedSearchForm(),
                'search_bar': SearchForm(), 
                }

    return render(request, "advanced_search.html", context)