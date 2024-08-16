from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
    item_objects = Item.objects.all()
    return render(request, template_name='main/index.html', context={'item_objects': item_objects})

def item(request):
    return HttpResponse("<h1>Hello Items!</h1>")

def detail(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'main/detail.html', context={'item': item})
