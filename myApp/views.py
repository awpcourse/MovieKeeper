from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from myApp.forms import MovieCommentForm
from  django.views.generic.base import TemplateView
from myApp.models import Movie, WatchList


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
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'search.html', context_dict)

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
    template_name = 'index.html'

    def get(self, request):

        user=request.user

        movies=WatchList.objects.get(user=user)

        movieSeen = movies.movie
        context_dict = {
            'nume' : movieSeen.name,
            'genre': movieSeen.genre,
            'duration' : movieSeen.duration
        }

        return render(request, self.template_name, context_dict)
