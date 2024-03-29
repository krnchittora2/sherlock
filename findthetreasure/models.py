from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Static Models
class Character(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

class Location(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='location_images/', null=True, blank=True)

class Treasure(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    value = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='treasure_images/', null=True, blank=True)

# Game Models
class Player(User):
    legalname = models.TextField(null=False, blank=False)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True, blank=False)

class GameProgress(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    player = models.OneToOneField(Player, on_delete=models.CASCADE, unique=True)
    current_location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True)
    acquired_treasures = models.ManyToManyField('Treasure', blank=True)
    score = models.IntegerField(default=0)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Game Progress for {self.player.username}"
    
