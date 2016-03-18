from django.shortcuts import render

from .models import Song, Composer, Book
# Create your views here.
def all_songs(request):
	songs = Song.objects.all().order_by('name')
	context = { 'songs': songs }
	
	# Passes variables to home.html through context list of variables
	return render(request, "songsall.html", context)

def single_song(request, songslug):
	song = Song.objects.get(slug=songslug)
	context = { 'song': song }
	return render(request, "singlesong.html", context)


def composer_page(request, composerslug):
	composer = Composer.objects.get(slug=composerslug)
	composer_songs = Song.objects.all().filter(composer__slug=composerslug)
	context = { 'composer': composer, 'composer_songs': composer_songs }
	return render(request, "composer.html", context)

def single_book(request, bookslug):
	book = Book.objects.get(slug=bookslug)
	
	context = { 'book': book }
	return render(request, "singlebook.html", context)

def search_query(request):
	form = SearchBar(request.POST or None)

	return render(request, "search_results", context)

