from rest_framework import serializers

from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField(max_length=100, required=True)
    social_link = serializers.URLField(max_length=200, required=True)
    class Meta:
        model = Artist
        fields = '__all__'