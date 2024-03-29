from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PlayerRegistrationForm
from .models import Character, Player

def register(request):
    if(request.user.is_authenticated):
        return redirect('select_character')
    players = Player.objects.all()

    if request.method == 'POST':
        # Login form submitted
        if 'player_login' in request.POST:
            inputuser = request.POST.get('username')
            player = Player.objects.get(username=inputuser)
            if player is not None:
                login(request, player)
                print('Player Logged in: ', inputuser)
                return redirect('select_character')
            return render(request, 'register.html', {'players': players, 'error_message': 'Player Not Found.'})
        
        # Registration form submitted
        elif 'player_register' in request.POST:
            form = PlayerRegistrationForm(request.POST)
            if form.is_valid():
                inputuser = form.cleaned_data['username']
                if(inputuser is not None and inputuser!=''):
                    player = form.save(commit=False)
                    player.save()
                    login(request, player)
                    return redirect('select_character')
                else:
                    return render(request, 'register.html', {'players': players, 'error_message': 'The provided username is not valid.'})
            else:
                return render(request, 'register.html', {'players': players, 'error_message': form.errors.as_text()})
        
        else:
            return render(request, 'register.html', {'players': players, 'error_message': 'Invalid Request.'})
    return render(request, 'register.html', {'players': players})

def player_logout(request):
    print('Logging out: ', request.user)
    logout(request)
    return redirect('register')

def select_character(request):
    characters = Character.objects.all()
    if request.method == 'POST':
        character_id = request.POST.get('character')
        character = Character.objects.get(id=character_id)
        player = Player.objects.get(username=request.user.username)
        if player:
            player.character = character
            player.save()
            return redirect('start_game')
    else:
        if(request.user.is_authenticated):
            player = Player.objects.get(username=request.user.username)
            if player.character is None:
                return render(request, 'select_character.html', {'characters': characters})
            else:
                return redirect('start_game')
    return redirect('register')

def start_game(request):
    player = Player.objects.get(username=request.user.username)
    return render(request, 'start_game.html', {'player': player})

def next_step(request):
    message = "Congratulations! You've taken the next step in the game."
    return HttpResponse(message)