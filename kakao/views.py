from django.shortcuts import render
from django.http import JsonResponse
from . import api
import json

# Create your views here.

def translate(request):
    request_json = json.loads(request.body)
    text = request_json['action']['params']['text']['value']
    return JsonResponse(api.kr_to_en(text))