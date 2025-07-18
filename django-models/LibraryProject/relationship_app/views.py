from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book, UserProfile
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required



def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


def list_books(request) :
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView) :
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list-books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

