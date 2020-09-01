from django.urls import path

from . import views

app_name = 'kakao'

urlpatterns = [
    # /kakao/
#    path('', views.IndexView.as_view(), name='index'),
    # /kakao/translate/
    path('translate/', views.translate, name='translate'),
]