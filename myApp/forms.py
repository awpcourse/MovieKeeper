from django.forms import Form, CharField, Textarea


class MovieCommentForm(Form):
    comment_text = CharField(widget=Textarea(
        attrs={'cols': 50, 'rows': 4, 'placeholder': 'Write a comment...'}),
        label='')