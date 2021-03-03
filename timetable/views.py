import datetime

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from timetable.web import get_plawecki

from timetable.web.scraper import get_timetable_solak


def server_test(request):
    return HttpResponse("server working...")


@api_view(['GET'])
def get_response_timetable_plawecki(requset, direction):
    timetable_get = get_plawecki.get_timetable_plawecki(direction)
    return JsonResponse(timetable_get, safe=False)


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
