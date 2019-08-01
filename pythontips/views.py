# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# pylint: disable=no-member

# import tweepy
import sqlite3
from django.shortcuts import render
from . import tweepy
#  import OAuthHandler

from django.http import HttpResponse

from .models import Tip

# Create your views here.

def index(request):
    return HttpResponse('<h1>Welcome to Python Tips! </h1> <i> ... curated by Obafemi<i>')
    # return HttpResponse('Welcome to Python Tips')

def showTip(request):
    # def showTip(request, tip_id):
    tips = Tip.objects.all().order_by('tip_timestamp')
    # return HttpResponse(tips)
    return render(request, 'pythontips/index.html', {'tips': tips})
    # return HttpResponse('Here is tip with ID: %s', tips)

def showTipLinks(request, tip_id):
    return HttpResponse('Here is links for tip with ID: %s', tip_id)

def create(tip_timestamp, tip_text, tip_link, tip_author, tip_published):
    newTip = Tip.objects.create(tip_timestamp=tip_timestamp, tip_text=tip_text, tip_link=tip_link, tip_author=tip_author, tip_published=tip_published)
    # newTip.save()
    # return render(request, showTip, {'tips': tips})
    return newTip

def loadTips(request):
    # from tweepy import OAuthHandler, API
    # Authenticate to Twitter
    # auth = tweepy.OAuthHandler("lJ2qmapBCAvUXabumToFA8nny",
    #                         "KpWixWjG5KsQ26OUkzHLuPQCFnbncb2qbVf9FdwLuEQhs2SUYK")
    # auth.set_access_token("1376361980-1YVxPEa7A54QEXO6Yr60bZyAnW7vZakMeQBQPy0",
    #                     "E6BH0eY5x4uJagVR9439ATC02VmRPnUt2OXan2QPzmSCQ")

    # api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # try:
    #     api.verify_credentials()
    #     tweets = api.user_timeline('python_tip')
    #     for tweet in tweets:
    #         print(tweet)
    #     print("Authentication OK")
    # except:
    #     print("Error during authentication")
    return HttpResponse('<h1>Loading new Tips now!!!</h1>')
