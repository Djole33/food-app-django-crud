from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterFrom

# Create your views here.

def register(request):
    form = RegisterFrom()   
    if request.method == "POST":
        form = RegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome, {username}!')
            return redirect('/login')
    return render(request, 'users/register.html', {'form': form})
