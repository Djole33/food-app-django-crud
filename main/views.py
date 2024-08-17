from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.

def index(request):
    item_objects = Item.objects.all()
    return render(request, template_name='main/index.html', context={'item_objects': item_objects})

def item(request):
    return HttpResponse("<h1>Hello Items!</h1>")

def detail(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'main/detail.html', context={'item': item})

def create_item(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'main/create-item.html', context={'form': form})

def edit_item(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, 'main/edit-item.html', context={'form': form})

def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('/')
