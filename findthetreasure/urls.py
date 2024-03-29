
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('player-logout/', views.player_logout, name='player_logout'),
    path('select-character/', views.select_character, name='select_character'),
    path('start-game/', views.start_game, name='start_game'),
    path('next-step/', views.next_step, name='next_step')
]