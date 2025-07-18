from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book 
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def list_books(request) :
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView) :
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


class CustomLoginView(LoginView) :
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView) :
    template_name = 'relationship_app/logout.html'


class RegisterView(CreateView) :
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')




