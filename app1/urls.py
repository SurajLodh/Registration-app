from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home),
    path('register/', views.Register),
    # path('', django.contrib.auth.urls),
    # path('login/', views.Login),
]
