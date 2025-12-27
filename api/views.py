from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Movies, Series, Genre
from .serializers import *

# Create your views here.

@api_view(['GET'])
def movies_list(request):
    movies = get_list_or_404(Movies)
    serializer = MovieSerializer(movies, many=True)
    return Response({"Peliculas": serializer.data}, status=200)

@api_view(['GET'])    
def series_list(request):
    series = get_list_or_404(Series)
    serializer = SeriesSerializer(series, many=True)
    return Response({"Series": serializer.data}, status=200)
    
@api_view(['GET'])
def movie_detail(request, id):
    movie = get_object_or_404(Movies, pk=id)
    serializer = MovieSerializer(movie)
    return Response({"Pelicula": serializer.data}, status=200)

@api_view(['GET'])
def serie_detail(request, id):
    serie = get_object_or_404(Series, pk=id)
    serializer = SeriesSerializer(serie)
    return Response({"Serie": serializer.data}, 200)

@api_view(['GET'])
def movies_genre(request, genre):
    movies = Movies.objects.filter(base__genres__name=genre)
    if not movies.exists():
        return Response(
            {"error": f"No hay películas del género {genre}"},
            status=404
        )
    serializer = MovieSerializer(movies, many=True)
    return Response({"Peliculas": serializer.data}, status=200)


@api_view(['GET'])
def series_genre(request, genre):
    series = Series.objects.filter(base__genres__name=genre)
    if not series.exists():
        return Response(
            {"error": f"No hay series del género {genre}"},
            status=404
        )
    serializer = SeriesSerializer(series, many=True)
    return Response({"Series": serializer.data}, status=200)
    


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_movie(request):
    serializer = MovieCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    movie = serializer.save()
    return Response(MovieSerializer(movie).data, status=201)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_serie(request):
    serializer = SerieCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serie = serializer.save()
    return Response(SeriesSerializer(serie).data, status=201)

@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def update_movie(request, id):
    movie = get_object_or_404(Movies, pk=id)
    base = movie.base
    serializer = MovieUpdateSerializer(
        data = request.data,
        partial = True
    )
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    if "title" in data:
        base.title = data["title"]
        
    if "genres" in data:
        for name in data["genres"]:
            genre, _ = Genre.objects.get_or_create(name=name)
            base.genres.add(genre)
            
    base.save()
    
    for field in ["year", "director", "duration_minutes"]:
        if field in data:
            setattr(movie, field, data[field])
            
    movie.save()
    
    return Response(MovieSerializer(movie).data)


@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def update_serie(request, id):
    serie = get_object_or_404(Series, pk=id)
    base = serie.base
    serializer = SerieUpdateSerializer(
        data = request.data,
        partial = True
    )
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    
    if "title" in data:
        base.title = data["title"]
    
    if "genres" in data:
        for name in data["genres"]:
            genre, _ = Genre.objects.get_or_create(name=name)
            base.genres.add(genre)
    
    base.save()
    
    for field in ["start_year", "end_year", "season_count", "episodes_count"]:
        if field in data:
            setattr(serie, field, data[field])
            
    serie.save()
    
    return Response(SeriesSerializer(serie).data)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_movie(request, id):
    movie = get_object_or_404(Movies, pk=id)
    movie.delete()
    return Response(status=204)



@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_serie(request, id):
    serie = get_object_or_404(Series, pk=id)
    serie.delete()
    return Response(status=204)