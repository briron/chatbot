from django.shortcuts import render
from django.http import JsonResponse
from . import api

# Create your views here.

def translate(request):
    print(type(request.POST))
    text = request.POST['action']['params']['text']['value']
    return JsonResponse(api.kr_to_en(text))