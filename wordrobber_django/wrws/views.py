from django.http import HttpResponse
import simplejson
import time
import base64
import os
import random
from models import *
from django.core import serializers
from django.http import Http404
from django.contrib.auth.models import check_password

def login(request):
    '''
    check username and password in the database. If they match, then
    generate a unique token (nonce) and a timestamp.
    '''
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
 
        try:
            user = User.objects.get(username=username)
        except:
            raise Http404


        sessionid = base64.b64encode(os.urandom(16))
        timestamp = time.time()
        
        data = simplejson.dumps({"sessionid": sessionid,"timestamp": timestamp})
        return HttpResponse(data, mimetype="application/json")
    else:
        # change to a better error handling mechanism
        return HttpResponse(None, mimetype="application/json")

def json_game(game):
    game_dict = dict()
    game_dict["name"] = game.name
    game_dict["description"] = game.description
    game_dict["help_text"] = game.help_text
    game_dict["drawer_size"] = game.drawer_size
    return game_dict

def games(request):
    games = dict()
    for game in Game.objects.all(): 
        games[game.id] = json_game(game)
    data = simplejson.dumps(games)
    return HttpResponse(data, mimetype="application/json")
    
def game(request, _name):
    try:
        game = Game.objects.get(name = _name)
    except:
        raise Http404

    data = simplejson.dumps(json_game(game))
    return HttpResponse(data, mimetype="application/json")

def json_player(player):
    player_dict = dict()
    player_dict["username"] = player.user.username
    player_dict["name"] = player.name
    player_dict["about"] = player.about
    return player_dict
   
def player(request, _username):
    try:
        user = User.objects.get(username = _username)
        player = Player.objects.get(user = user)
    except:
        raise Http404

    data = simplejson.dumps(json_player(player))
    return HttpResponse(data, mimetype="application/json")
   
def json_question(question,choices):
    question_dict = dict()
    question_dict["text"] = question.text
    
    choice_dict = dict()
    for choice in choices:
        choice_dict[choice.id] = choice.text
    
    question_dict["choices"] = choice_dict
    return question_dict
   
def question(request):
    if request.GET:
        game_id = request.GET["game"]
    else:
        raise Http404
    
    game = Game.objects.get(name=game_id)
    questions = Question.objects.filter(game=game)
    print questions
    # TODO: now a random question is picked up.
    # this has to be random, excluding the questions the player have already
    # given an answer to.
    question = random.choice(questions)
    
    choices = Choice.objects.filter(question=question)
    data = simplejson.dumps(json_question(question,choices))
    return HttpResponse(data, mimetype="application/json")
