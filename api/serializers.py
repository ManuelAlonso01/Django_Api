from rest_framework import serializers
from .models import Movies, Series, Base, Genre
    
class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="base.title")
    genres = serializers.SlugRelatedField(
        source="base.genres",
        many=True,
        read_only=True,
        slug_field="name",
    )
    class Meta:
        model = Movies
        fields = [
            "id",
            "title",
            "genres",
            "year",
            "director",
            "duration_minutes",
        ]
    
            
class SeriesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="base.title")
    genres = serializers.SlugRelatedField(
        source="base.genres",
        many=True,
        read_only=True,
        slug_field="name",
    )
    class Meta:
        model = Series
        fields = [
            "id",
            "title",
            "genres",
            "start_year",
            "end_year",
            "season_count",
            "episodes_count",
        ]
    
class MovieCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    genres = serializers.ListField(
        child = serializers.CharField()
    )
    year = serializers.IntegerField()
    director = serializers.CharField()
    duration_minutes = serializers.IntegerField()
    
    def validate_title(self, value):
        return value.strip().title()
    
    def validate_director(self, value):
        return value.strip().title()
    
    def validate_genres(self, value):
        return [g.strip().lower() for g in value]
    
    def create(self, valited_data):
        genres_names = valited_data.pop("genres")
        base = Base.objects.create(
            title = valited_data["title"],
            tipo = "movie"
        )
        for name in genres_names:
            genre, _ = Genre.objects.get_or_create(name=name)
            base.genres.add(genre)
        
        movie = Movies.objects.create(
            base=base,
            year = valited_data["year"],
            director = valited_data["director"],
            duration_minutes = valited_data["duration_minutes"],
        )
        return movie
    
class SerieCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    genres = serializers.ListField(
        child = serializers.CharField()
    )
    start_year = serializers.IntegerField()
    end_year = serializers.IntegerField()
    season_count = serializers.IntegerField()
    episodes_count = serializers.IntegerField()
    
    def validate_title(self, value):
        return value.strip().title()
    
    def validate_genres(self, value):
        return [g.strip().lower() for g in value]
    
    def create(self, valited_data):
        genres_names = valited_data.pop("genres")
        base = Base.objects.create(
            title = valited_data["title"],
            tipo = "serie"
        )
        for name in genres_names:
            genre, _ = Genre.objects.get_or_create(name=name)
            base.genres.add(genre)
        
        serie = Series.objects.create(
            base=base,
            start_year = valited_data["start_year"],
            end_year = valited_data["end_year"],
            season_count = valited_data["season_count"],
            episodes_count = valited_data["episodes_count"],
        )
        return serie

class MovieUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    genres = serializers.ListField(
        child = serializers.CharField(),
        required = False
    )
    year = serializers.IntegerField(required=False)
    director = serializers.CharField(required=False)
    duration_minutes = serializers.IntegerField(required=False)
    
class SerieUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    genres = serializers.ListField(
        child = serializers.CharField(),
        required = False
    )
    start_year = serializers.IntegerField(required=False)
    end_year = serializers.IntegerField(required=False)
    season_count = serializers.IntegerField(required=False)
    episodes_count = serializers.IntegerField(required=False)