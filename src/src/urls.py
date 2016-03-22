from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^songs/$', 'piano.views.all_songs', name='all_songs'),
    url(r'^songs/(?P<songslug>.*)/$', 'piano.views.single_song', name='single_song'),
    url(r'^composers/(?P<composerslug>.*)/$', 'piano.views.composer_page', name='composer_page'),
    url(r'^books/(?P<bookslug>.*)/$', 'piano.views.single_book', name='single_book'),

    # url(r'^results_of_search/$', 'piano.views.get_search', name='get_search'),

    url(r'^$', 'piano.views.home', name='home'),
    url(r'^submit_an_entry/$', 'piano.views.submit_an_entry', name='submit_an_entry'),

    url(r'^advanced_search$', 'piano.views.advanced_search', name='advanced_search'),

    url(r'^admin/', include(admin.site.urls)),

]
