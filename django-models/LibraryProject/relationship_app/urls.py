from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view



urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    #Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), redirect_authenticated_user=True, name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), redirect_authenticated_user=True, name='logout'),
    path('register/', views.register, name='register'),

    path('admin/',views. admin_view, name='admin_dashboard'),
    path('librarian/', views.librarian_view, name='librarian_dashboard'),
    path('member/', views.member_view, name='member_dashboard'),
]