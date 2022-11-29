from django.shortcuts import render, redirect

from django.contrib.auth import login
from .forms import UserRegistrationForm
# Create your views here.


def on_sayfa(request):
    return render(request, 'on_sayfa.html')


def kayit(request):
    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('on_sayfa')
    
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'kayit.html', context)
