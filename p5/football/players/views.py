from django.shortcuts import render
from .models import teams

def show_players(request):
    context = {}
    context[ 'team' ] = teams.objects.all()
    return render(request, 'players/show_players.html',context)



