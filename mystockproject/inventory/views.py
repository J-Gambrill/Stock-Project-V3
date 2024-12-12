from django.shortcuts import render
from .models import Stock

# Create your views here.
def stock_list(request):
    inventory = Stock.objects.all().order_by('-createdAt') # orders in a decending order of date
    return render(request, 'inventory/stock_list.html', { 'inventory': inventory }) # links to the folder and then the page in order

def item_page(request, slug): #recieved slug from urls.py
    stock = Stock.objects.get(slug=slug)
    return render(request, 'inventory/item_page.html', {'stock': stock})