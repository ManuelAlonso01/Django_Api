from django.urls import path
from .views import *

urlpatterns = [
    #<-----------------GET------------------->
    path("movies/", movies_list),
    path("series/", series_list),
    path("movies/id/<int:id>/", movie_detail),
    path("series/id/<int:id>/", serie_detail),
    path("movies/genre/<str:genre>/", movies_genre),
    path("series/genre/<str:genre>/", series_genre),
    path("movies/title/<str:movie_title>/", find_movie_title),
    path("series/title/<str:serie_title>/", find_serie_title),
    
    #<-----------------POST------------------>
    path("movies/create/", create_movie),
    path("series/create/", create_serie),
    
    #<-----------------PATCH----------------->
    path("movies/update/<int:id>/", update_movie),
    path("series/update/<int:id>/", update_serie),
    
    #<-----------------DELETE---------------->
    path("movies/delete/<int:id>/", delete_movie),
    path("series/delete/<int:id>/", delete_serie),
]