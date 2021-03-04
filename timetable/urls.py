from django.urls import path

from . import views

urlpatterns = [
    path('', views.server_test),
    path('timetables/plawecki', views.get_response_timetable_plawecki_all),
    path('timetables/solak', views.get_response_timetable_solak_all),
    path('timetables/plawecki/<str:direction>', views.get_response_timetable_plawecki),
    path('timetables/solak/<str:direction>', views.get_response_timetable_solak),
    path('time/<str:time>/<str:direction>', views.get_close_time),
]
