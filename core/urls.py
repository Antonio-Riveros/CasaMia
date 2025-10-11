# core/urls.py
from django.urls import path
from . import views

app_name = 'core'  # o 'pages', según tu app

urlpatterns = [
    path('nosotros/', views.nosotros, name='nosotros'),
]