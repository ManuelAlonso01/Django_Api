from django.urls import path
from .views import *

urlpatterns = [
    path("movies/", movies_list),
    path("series/", series_list),
    path("movies/<int:id>/", movie_detail),
    path("series/<int:id>/", serie_detail),
    path("movies/create/", create_movie),
    path("series/create/", create_serie),
    path("movies/update/<int:id>/", update_movie),
    path("series/update/<int:id>/", update_serie),
    path("movies/delete/<int:id>/", delete_movie),
    path("series/delete/<int:id>/", delete_serie),
    path("movies/<str:genre>/", movies_genre),
    path("series/<str:genre>/", series_genre),
    
]