from rest_framework import serializers
from .models import Team, Player, Tournament, Match

class TeamSerializer(serializers.ModelSerializer): #класс сериализатора, который автоматом поставит все поля модели
    class Meta:
        model = Team        #which model to serialize
        fields = '__all__'  #which fields to choose

class PLayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'
        
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'