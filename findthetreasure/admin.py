from django.contrib import admin
from .models import Character, Location, Treasure

# Register your models here.

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'description')
    search_fields = ('name', 'role')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'city', 'country', 'image')
    search_fields = ('name', 'city', 'country')

@admin.register(Treasure)
class TreasureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'location', 'value', 'image')
    search_fields = ('name', 'location__name', 'value')