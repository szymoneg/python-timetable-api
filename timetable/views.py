from django.http import HttpResponse, JsonResponse
from timetable.scrapper import get_timetable_solak
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
import datetime


def server_test(request):
    return HttpResponse("server working...")


@api_view(['GET'])
def get_response_timetable_solak(request):
    timetable_get = get_timetable_solak()
    return JsonResponse(timetable_get, safe=False)


@api_view(['GET'])
def get_timetable_solak_oneway(request, direction):
    timetable_get = get_timetable_solak()[direction]
    return JsonResponse(timetable_get, safe=False)


@api_view(['GET'])
def get_close_time(request, time, direction):
    day = datetime.datetime.now().weekday()
    if 0 < day <= 4:
        hours = list(get_timetable_solak()[direction][0])
    elif day == 5:
        hours = list(get_timetable_solak()[direction][1])
    else:
        hours = list(get_timetable_solak()[direction][2])
    now = datetime.datetime.strptime(time, "%H:%M")
    # VVV
    closest_bus = min(hours, key=lambda t: abs(now - datetime.datetime.strptime(t, "%H:%M")))
    return JsonResponse(closest_bus, safe=False)
