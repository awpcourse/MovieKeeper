from django.shortcuts import render, redirect
from django.http import HttpResponse
from myApp.forms import MovieCommentForm, SearchMoviesForm
from .utils import getMovies
from myApp.models import Movie, WatchList, Comment
from django.views.generic import TemplateView
import datetime


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the
    # template!
    commentform = MovieCommentForm()
    context_dict = {
        'boldmessage': "I am bold font from the context",
        'commentform': commentform
    }

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'index.html', context_dict)


def search(request):
    search_form = SearchMoviesForm()
    searched=request.GET.get('search',None)
    myMovies=[]

    #Search movies on API
    myMovies=getMovies(searched)
    print myMovies
    # print myMovies #movie['long imdb canonical title'], movie.movieID
    # movies=[{"nume":"Mancare", "durata":120},{"nume":"test","durata":139}]
    context_dict = {
        'boldmessage': "I am bold font from the context",
        "movies":myMovies,
        'search_form': search_form
    }
    return render(request, 'search.html', context_dict)


class moviedetails(TemplateView):
    template_name = 'moviedetails.html'
    comments = Comment.objects.all()

    def get(self, request, id):
        movie = Movie.objects.get(pk=id)
        comments = Comment.objects.filter(movie_id=id)
        context = {
            'movie': movie,
            'comments': comments,
            'commentform': MovieCommentForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        form = MovieCommentForm(request.POST)
        movie = Movie.objects.get(pk=id)
        if form.is_valid():
            text = form.cleaned_data['comment_text']
            comment = Comment(comment=text, movie=movie,
                              user=request.user, dateTime=datetime.datetime.now())
            comment.save()
        return redirect('/moviedetails/{}'.format(id))


class SimulateWatchlist(TemplateView):
    template_name = 'index.html'

    def get(self, request, pk):

        movie = Movie.objects.get(pk=pk)
        user = request.user

        if WatchList.objects.filter(movie=movie, user=user).count() > 0:
            message = "Movie already in list!"
        else:
            watchlist = WatchList(movie=movie, user=request.user)
            watchlist.save()
            message = "Movie added to watchlist"

        context_dict = {
            'boldmessage': message
        }

        return render(request, self.template_name, context_dict)


class AllMoviesSeen(TemplateView):

    template_name = 'allMoviesSeen.html'

    def get(self, request):
        user = request.user
        movies = WatchList.objects.get(user=user)
        movies = WatchList.objects.filter(user=user).all()
        context_dict = {
            'nume': movieSeen.name,
            'genre': movieSeen.genre,
            'duration': movieSeen.duration,
            'movies': movies
        }
        return render(request, self.template_name, context_dict)
