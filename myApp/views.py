from django.shortcuts import render, redirect
from django.http import HttpResponse
from myApp.forms import MovieCommentForm
from django.views.generic import TemplateView
from myApp.models import Comment, Movie
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
    context_dict = {'boldmessage': "I am bold font from the context"}
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
            comment = Comment(comment=text, movie=movie, user = request.user, dateTime = datetime.datetime.now())
            comment.save()
        return redirect('/moviedetails/{}'.format(id))