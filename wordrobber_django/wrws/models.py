from django.db import models
from django.contrib.auth.models import User


def avatar_file_name(instance, filename):
    return "avatar/%s.jpg" % instance.user.username

def game_file_name(instance, filename):
    return "game_icons/%s.jpg" % instance.name

def achievement_file_name(instance, filename):
    return "achievement_icons/%s.jpg" % instance.shortname()
    
# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    about = models.TextField()
    avatar = models.ImageField(upload_to=avatar_file_name)
        
    def __unicode__(self):
        return self.user.username

class Game(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to=game_file_name)
    description = models.TextField()
    help_text = models.TextField(blank=True)
    drawer_size = models.IntegerField()
    
    def __unicode__(self):
        return self.name

class Question(models.Model):
    game = models.ForeignKey(Game)
    text = models.TextField()

    def __unicode__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    
    def __unicode__(self):
        return self.text

class Answer(models.Model):
    choice = models.ForeignKey(Choice)
    player = models.ForeignKey(Player)
    bet = models.IntegerField() 
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{0}: {1}" % (self.self.player, self.choice)

class Drawer(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{0}, {1}" % (self.self.player, self.game)
    

class Achievement(models.Model):
    game = models.ForeignKey(Game, null=True, blank=True)
    drawers = models.IntegerField()
    icon = models.ImageField(upload_to=achievement_file_name)
    TYPECHOICE = (
        ('total', 'Total drawers'),
        ('one', 'Specific game'),
        ('each', 'Minumin drawers (each game)'),
    )
    type = models.CharField(max_length=5, choices=TYPECHOICE)

    def shortname(self):
        if self.game:
            return "{0}{1}{2}" % (self.game, self.type, self.drawers)
        else:
            return "{0}{1}" % (self.type, self.drawers)


    def __unicode__(self):
        return "{0}, {1}" % (self.player, self.game)
    

