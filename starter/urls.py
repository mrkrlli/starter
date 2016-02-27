from django.conf.urls import patterns, include, url

from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = patterns(__package__ + '.views',
    url(r'^$', 'landing_page', {}, 'landing_page'),
    url(r'^movie_list/', views.movie_list, name='movie_list'),
    url(r'^movie_details/(?P<movie_id>[0-9]+)', views.movie_details, name='movie_details'),
    url(r'^admin/', include(admin.site.urls)),
)
	