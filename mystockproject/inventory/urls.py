from django.urls import path
from . import views  # links to views.py

app_name = 'inventory'

urlpatterns = [
    path('', views.stock_list, name = "list"), #this is the name of our link see layout.html 
    path('<slug:slug>', views.item_page, name = "page"),
]
