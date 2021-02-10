from django.urls import path

from . import views

urlpatterns = [
    path('', views.server_test),
    path('timetables/', views.get_response_timetable_solak),
    path('direction/<str:direction>', views.get_timetable_solak_oneway),
    path('time/<str:time>/<str:direction>', views.get_close_time)
]
