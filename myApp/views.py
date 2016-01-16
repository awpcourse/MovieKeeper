from django.shortcuts import render, redirect
from django.http import HttpResponse
from myApp.forms import MovieCommentForm, SearchMoviesForm
# from .utils import getMovies
from myApp.models import Movie, WatchList, Comment, WishList
from django.views.generic import TemplateView
import datetime
import random

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the
    # template!
    commentform = MovieCommentForm()
    

    movies_array = [{"imdbId":2488496,
            "name":'Star wars',
            "picture":"http://powet.tv/powetblog/wp-content/uploads/2006/09/starwars_cover.jpg",
            "duration":'02:35:00',
            "genre":"action",
            },{"imdbId":2488498,
            "name":'Titanic',
            "picture":"http://ecx.images-amazon.com/images/I/91rZp5zs8kL._SL1500_.jpg",
            "duration":'3:00:00',
            "genre":"Drama",
            },{"imdbId":2488496,
            "name":'The Shawshank Redemption',
            "picture":"https://upload.wikimedia.org/wikipedia/ro/thumb/c/cb/The_Shawshank_Redemption.jpg/250px-The_Shawshank_Redemption.jpg",
            "duration":'2:35:00',
            "genre":"Drama",
            },{"imdbId":2488494,
            "name":'Nea Marin Miliardar',
            "picture":"http://static.cinemarx.ro/poze/filme-mari/2009/05/Nea_Marin_miliardar_1241295304_1979.jpg",
            "duration":'2:15:00',
            "genre":"Comedy",
            },{"imdbId":2488436,
            "name":'Ice Age',
            "picture":"http://www.dvd-forum.at/img/uploaded/62072_d31e3679b132439fa536dc91a87fe0f0_2.jpg",
            "duration":'1:30:00',
            "genre":"Comedy",
            },{"imdbId":2488436,
            "name":'The Prestige',
            "picture":"http://images-eu.amazon.com/images/P/B00005JPBP.02.LZZZZZZZ.jpg",
            "duration":'2:35:00',
            "genre":"Drama"},{"imdbId":2488436,
            "name":'God father',
            "picture":"https://adrianazavoi.files.wordpress.com/2012/04/godfather.jpg",
            "duration":'1:45:00',
            "genre":"Drama"},{"imdbId":2488436,
            "name":'The Schindler"s List',
            "picture":"https://terrymalloyspigeoncoop.files.wordpress.com/2014/03/a80733tlh20.jpg",
            "duration":'2:25:00',
            "genre":"Comedy",
            },{"imdbId":2488436,
            "name":'The silence of the Lambs',
            "picture":"http://www.goldposter.com/wp-content/uploads/2015/04/The-Silence-of-the-Lambs_poster_goldposter_com_27.jpg",
            "duration":'1:30:00',
            "genre":"Action",
            },{"imdbId":2388436,
            "name":'Avatar',
            "picture":"http://resizing.flixster.com/W1BtrV4MS0HZwzJQSBe4mBQfwQs=/800x1200/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/67/11176792_ori.jpg",
            "duration":'2:15:00',
            "genre":"Drama",
            }]


    context_dict = {
        'boldmessage': "I am bold font from the context",
        'commentform': commentform,
        'movies' : random.sample(movies_array, 5)
    }
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'index.html', context_dict)


def search(request):
    search_form = SearchMoviesForm()
    searched=request.GET.get('search',None)
    myMovies=[]

    # Search movies on API
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

        movies = WatchList.objects.filter(user=user).all()
        
        context_dict = {
            'movies' : movies
            }
   
        return render(request, self.template_name, context_dict)

class AddToWishlist(TemplateView):

    template_name = 'index.html'

    def get(self, request, pk):

        movie = Movie.objects.get(pk=pk)
        user = request.user

        if WishList.objects.filter(movie=movie, user=user).count() > 0:
            message = "Movie already in list!"
        else:
            wishlist = WishList(movie=movie, user=request.user)
            wishlist.save()
            message = "Movie added to wishlist"
        
        context_dict = {
            'boldmessage': message 
        }
        return render(request, self.template_name, context_dict)

class MyWishlist(TemplateView):
    
    template_wishlist = 'wishlist.html'

    def get(self, request):

        user=request.user

        movies=WishList.objects.filter(user=user).all()

         
        context_dict = {
            'movies' : movies
            }
   
        return render(request, self.template_wishlist, context_dict)