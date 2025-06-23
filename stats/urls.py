from django.urls import path
from .views import (
    TeamListCreateAPIView, TeamRetrieveUpdateDestroyAPIView, 
    PlayerListCreateAPIView, PlayerRetrieveUpdateDestroyAPIView,
    TournamentListCreateAPIView, TournamentRetrieveUpdateDestroyAPIView,
    MatchListCreateAPIView, MatchRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    path('teams', TeamListCreateAPIView.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamRetrieveUpdateDestroyAPIView.as_view(), name='team-detail'),

    path('players', PlayerListCreateAPIView.as_view(), name='player-list-create'),
    path('players/<int:pk>/', PlayerRetrieveUpdateDestroyAPIView.as_view(), name='player-detail'),

    path('tournament', TournamentListCreateAPIView.as_view(), name='tournament-list-create'),
    path('players/<int:pk>/',TournamentRetrieveUpdateDestroyAPIView.as_view(), name='tournament-detail'),

    path('match', MatchListCreateAPIView.as_view(), name='match-list-create'),
    path('match', MatchRetrieveUpdateDestroyAPIView.as_view, name='match-detail')
]
