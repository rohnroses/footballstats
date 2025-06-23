from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    logo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name 
    
class Player(models.Model):
    POSITION_CHOICES = [
         ('GK', 'Goalkeeper'),
         ('DEF', 'Defender'),
         ('MID', 'Midfielder'),
         ('FWD', 'Forward'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    position = models.CharField(max_length = 3, choices=POSITION_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return self.name
    
class Tournament(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)  # Турнир, в котором проходит матч
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')  # Первая команда (домашняя)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')  # Вторая команда (гостевая)
    date = models.DateField()  # Дата матча
    score_team1 = models.PositiveIntegerField(default=0)  # Голы первой команды
    score_team2 = models.PositiveIntegerField(default=0)  # Голы второй команды

    def __str__(self):
        return f"{self.team1} vs {self.team2} ({self.date})"
