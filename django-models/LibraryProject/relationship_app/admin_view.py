from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from .models import UserProfile

def is_admin(user):
    user.UserProfile.role == 'Admin'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")