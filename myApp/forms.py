from django.forms import Form, CharField, Textarea


class MovieCommentForm(Form):
    comment_text = CharField(widget=Textarea(
        attrs={'cols': 50, 'rows': 4, 'placeholder': 'Write a comment...', 'class': 'form-control'}),
        label='')


class SearchMoviesForm(Form):
    search = CharField(label="Search movies:", widget=Textarea(attrs={'cols': 20, 'rows': 1, 'class': 'form-control'}))
