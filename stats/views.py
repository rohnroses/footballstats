from django.shortcuts import render
from rest_framework import generics
from .models import Team, Player, Tournament, Match
from .serializers import TeamSerializer, PLayerSerializer, TournamentSerializer, MatchSerializer

class TeamListCreateAPIView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PLayerSerializer

class PlayerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PLayerSerializer

class TournamentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tournament.objects.all()
    serializer_class = Tournament.objects.all()

class TournamentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class MatchListCreateAPIView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MatchRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

