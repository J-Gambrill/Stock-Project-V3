from django.shortcuts import render, redirect
from .models import Stock
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url="/users/login/")
def stock_list(request):
    inventory = Stock.objects.all().order_by('-createdAt') # orders in a decending order of date
    return render(request, 'inventory/stock_list.html', { 'inventory': inventory }) # links to the folder and then the page in order

@login_required(login_url="/users/login/")
def item_page(request, slug): #recieved slug from urls.py
    stock = Stock.objects.get(slug=slug)
    return render(request, 'inventory/item_page.html', {'stock': stock})

@login_required(login_url="/users/login/")
def item_create(request):
    if request.method == 'POST':
       form = forms.CreateRequest(request.POST, request.FILES) #request.FILES is due to the image file being submitted
       if form.is_valid():
           createItem = form.save(commit=False)
           createItem.createdBy = request.user
           createItem.save()
           return redirect('inventory:list')
    else:
        form = forms.CreateRequest()
    return render(request, 'inventory/item_create.html', {'form': form})