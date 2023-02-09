from django.db import models

# Create your models here.


class Player(models.Model):
    '''Model for NHL players'''
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    team = models.ForeignKey("hockey.Team", on_delete=models.SET_NULL, related_name="players", null=True)
    number = models.IntegerField()
    height = models.CharField(max_length=100)
    weight = models.IntegerField()
    image = models.CharField(max_length=100)


class Team(models.Model):
    '''Model for NHL teams'''
    name = models.CharField(max_length=100)
    user = models.OneToOneField("nhl_auth.NHLUser", on_delete=models.CASCADE, related_name="team")
    city = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=3)
    division = models.CharField(max_length=100)
    conference = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    
