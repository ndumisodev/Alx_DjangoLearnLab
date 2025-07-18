from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import View

def check_admin(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'ADMIN'

def check_librarian(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'LIBRARIAN'

def check_member(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'MEMBER'

@login_required
@user_passes_test(check_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(check_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Alternative class-based views
class AdminView(UserPassesTestMixin, View):
    def test_func(self):
        return check_admin(self.request.user)
    
    def get(self, request):
        return render(request, 'relationship_app/admin_view.html')

class LibrarianView(UserPassesTestMixin, View):
    def test_func(self):
        return check_librarian(self.request.user)
    
    def get(self, request):
        return render(request, 'relationship_app/librarian_view.html')

class MemberView(UserPassesTestMixin, View):
    def test_func(self):
        return check_member(self.request.user)
    
    def get(self, request):
        return render(request, 'relationship_app/member_view.html')