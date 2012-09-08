from django.http import HttpResponse
import simplejson
from models import *
from django.contrib.auth.models import User

def load_test_data(request):
    # delete existing objects, except admin user
    Player.objects.all().delete()
           
    User.objects.exclude(username='admin').delete()
    
    Choice.objects.all().delete()
    Question.objects.all().delete()
    Game.objects.all().delete()
    
    # how many test objects?
    n_players = 3
    n_games = 2
    n_questions = 10
    n_choices = 4
    drawer_size = 10
    
    # create test objects
    for i in range(n_players):
        user = User()
        user.username = "user{0}".format(i)
        user.save()
        
        player = Player()
        player.name = "Player {0}".format(i)
        player.user = user
        player.save()
        
    for i in range(n_games):
        game = Game()
        game.name = "Game {0}".format(i)
        game.drawer_size = drawer_size
        game.save()
        
        for j in range(n_questions):
            question = Question()
            question.game = game
            question.text = "Question {0}".format(i*n_questions+j)
            question.save()
            
            for k in range(n_choices):
                choice = Choice()
                choice.question = question
                choice.text = "Choice {0}".format((i*n_questions+j)*n_choices+k)
                choice.save(0)
    
    return HttpResponse(None, mimetype="application/json")
