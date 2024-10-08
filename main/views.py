from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

def index(request):
    item_objects = Item.objects.all()
    return render(request, template_name='main/index.html', context={'item_objects': item_objects})

class IndexClassView(ListView):
    model = Item
    template_name = 'main/index.html'
    context_object_name = 'item'

def item(request):
    return HttpResponse("<h1>Hello Items!</h1>")

def detail(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'main/detail.html', context={'item': item})

class FoodDetail(DetailView):
    model = Item
    template_name = 'main/detail.html'

def create_item(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'main/create-item.html', context={'form': form})

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'main/create-item.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

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

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')
