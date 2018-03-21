from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ml.analyzer import Analyzer

a = Analyzer()

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        return render(request, 'sentiment_api/index.html')
    elif request.method == 'POST':
        tweets = request.data['tweets']
        return Response(a.analyze(tweets))
