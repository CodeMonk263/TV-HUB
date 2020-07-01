from rest_framework import serializers, fields
from .models import *

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowsModel
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonModel
        fields = '__all__'

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodesModel
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }
