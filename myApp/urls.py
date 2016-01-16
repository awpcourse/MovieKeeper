from django.conf.urls import patterns, url
from myApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^search/$', views.search, name='search'),
        url(r'^simulate/(?P<pk>[0-9]+)$', views.SimulateWatchlist.as_view(), name='AddToWatchlist'),
        url(r'^allmovieseen/$', views.AllMoviesSeen.as_view(), name='MoviesSeen'))