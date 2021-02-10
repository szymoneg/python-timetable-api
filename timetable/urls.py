from django.urls import path

from . import views

urlpatterns = [
    path('', views.server_test),
    path('timetables/', views.get_response_timetable_solak)
]
