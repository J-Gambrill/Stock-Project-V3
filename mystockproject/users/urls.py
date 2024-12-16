from django.urls import path
from . import views  # links to views.py

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name = "register"), #this is the name of our link see layout.html 
]
