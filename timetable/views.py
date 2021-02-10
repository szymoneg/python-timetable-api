from django.http import HttpResponse, JsonResponse
from timetable.scrapper import get_timetable_solak
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status


def server_test(request):
    return HttpResponse("server working...")


def get_response_timetable_solak(request):
    timetable_get = get_timetable_solak()
    return JsonResponse(timetable_get, safe=False)