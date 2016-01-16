from django.contrib import admin
from myApp.models import Movie, Comment, WishList, WatchList

# Register your models here.
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(WishList)
admin.site.register(WatchList)