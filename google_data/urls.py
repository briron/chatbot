from django.urls import path

from . import views

app_name = 'google_data'

urlpatterns = [
    # /google_data/
    path('', views.index, name='index'),
    # /google_data/activity/
    path('activity/', views.visualizeTopCountApp, name='visualizeTopCountApp'),
]