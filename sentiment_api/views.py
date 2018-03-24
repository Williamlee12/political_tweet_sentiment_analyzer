from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ml.analyzer import Analyzer
from .twitter_api.twitter import Get_list_of_user_tweets

a = Analyzer()
t = Get_list_of_user_tweets()


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        return render(request, 'sentiment_api/index.html')
    elif request.method == 'POST':
        tweets = request.data['tweets']
        return Response(a.analyze(tweets))

@api_view(['GET', 'POST'])
def twitter(request):
    if request.method == 'GET':
        return render(request, 'sentiment_api/twitter.html')
    else:
        tweets = t.get_list(request.data["twitter_handle"])
        return Response(a.analyze(tweets))
