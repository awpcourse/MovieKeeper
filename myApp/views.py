from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from myApp.forms import MovieCommentForm


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