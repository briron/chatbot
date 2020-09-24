from django.shortcuts import render
from django.http import JsonResponse
from . import api, bot
import json

# Create your views here.


def translate(request):
    request_json = json.loads(request.body)
    request_text = request_json['action']['params']['text']
    response_text = api.kr_to_en(request_text)
    response_dict = bot.simpleText(response_text)
    return JsonResponse(response_dict)