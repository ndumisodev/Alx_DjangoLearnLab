from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    list_books, 
    LibraryDetailView,
)
from . import views

from . import admin_view


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    #Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), redirect_authenticated_user=True, name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), redirect_authenticated_user=True, name='logout'),
    path('register/', views.register, name='register'),

    # Function-based views
    path('admin/', admin_view.Admin, name='admin-view'),
    # path('librarian/', librarian_view, name='librarian-view'),
    # path('member/', member_view, name='member-view'),
]