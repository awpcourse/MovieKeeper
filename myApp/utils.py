import imdb

def getMovies(title):
    if title==None:
        return []

    ia=imdb.IMDb()
    myMovies=[]
    movies=ia.search_movie(title)
    for movie in movies:
        # mov=ia.get_movie('0133093')
        # print mov['director']
        
        myMovies.append({
            "imdbId":movie.movieID,
            "name":movie['long imdb canonical title'],
            "picture":"",
            "duration":0,
            "genre":"",
            })

    return myMovies