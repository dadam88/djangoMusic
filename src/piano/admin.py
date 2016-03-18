from django.contrib import admin

# Register your models here.
from .models import Song, Composer, Book

class SongAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('name', 'composer', 'books', 'level')
	# Must use foreignkey__attribute of child
	search_fields = ['name', 'composer__name', 'books__name', 'level']

class ComposerAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class BookAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Song, SongAdmin)
admin.site.register(Composer, ComposerAdmin)	
admin.site.register(Book, BookAdmin)