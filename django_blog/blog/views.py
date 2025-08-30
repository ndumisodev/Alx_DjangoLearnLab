from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog-home') # Redirect to your homepage
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})