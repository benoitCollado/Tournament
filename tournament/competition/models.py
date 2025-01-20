from typing_extensions import Required
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Competition(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(null = True)
  start_date = models.DateTimeField(default = 'django.utils.timezone.now')
  end_date = models.DateTimeField(null = True)
  organizer_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  created_at = models.DateTimeField(default = 'django.utils.timezone.now')
  updated_at = models.DateTimeField(default = 'django.utils.timezone.now')


class Team(models.Model):
  name = models.CharField(max_length=100)
  Competition_id = models.ForeignKey(Competition, on_delete=models.DO_NOTHING)
  created_at = models.DateTimeField(default = 'django.utils.timezone.now')
  updated_at = models.DateTimeField(default = 'django.utils.timezone.now')


class Participant(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  team_id = models.ForeignKey(Team, on_delete=models.DO_NOTHING)


STATUS_CHOICES = [
    ('scheduled', 'scheduled'),
    ('ongoing', 'ongoing'),
    ('finished', 'finished'),
]

class Match(models.Model):
  competition_id = models.ForeignKey(Competition, on_delete=models.DO_NOTHING)
  team1_id = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name = "team1")
  team2_id = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name = "team2")
  score_team1 = models.IntegerField(default=0)
  score_team2 = models.IntegerField(default=0)
  status = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='scheduled')
  scheduled_date = models.DateTimeField(default = 'django.utils.timezone.now')
  created_at = models.DateTimeField(default = 'django.utils.timezone.now')
  updated_at = models.DateTimeField(default = 'django.utils.timezone.now')
