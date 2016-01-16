from django.conf.urls import patterns, url
from myApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^search/$', views.search, name='search'),
        url(r'^moviedetails/(?P<id>\d+)', views.moviedetails.as_view(), name="moviedetails"))
