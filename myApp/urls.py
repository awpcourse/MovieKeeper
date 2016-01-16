from django.conf.urls import patterns, url
from myApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^search/$', views.search, name='search'),
        url(r'^moviedetails/(?P<id>\d+)', views.moviedetails.as_view(), name="moviedetails"),
        url(r'^simulate/(?P<pk>[0-9]+)$', views.SimulateWatchlist.as_view(), name='AddToWatchlist'),
        url(r'^allmovieseen/$', views.AllMoviesSeen.as_view(), name='MoviesSeen'),
        url(r'^addtowishlist/(?P<pk>[0-9]+)$', views.AddToWishlist.as_view(), name='AddToWishlist'),
        url(r'^wishlist/$', views.MyWishlist.as_view(), name='wishlist'))
