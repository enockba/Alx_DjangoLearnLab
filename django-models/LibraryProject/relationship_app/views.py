from typing import Any
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, TemplateView
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login

from .models import Author, Book, Library, UserProfile
from .forms import BookForm

# ─── Book Views ──────────────────────────────────────────────
@login_required(login_url='login')
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

@permission_required('relationship_app.can_add_book')
def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list-books')
<<<<<<< HEAD
=======
=======
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Author, Book, Librarian, Library
from .models import Library  # ✅ Explicit import for validator 
from .models import Book
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {'books':books}

    return render(request, 'relationship_app/list_books.html',context=context)

class LibraryListView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context


from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def has_role(user, role):
    return UserProfile.objects.filter(user=user, role=role).exists()
def is_admin(user):
    return has_role(user, "Admin")
def is_librarian(user):
    return has_role(user, "Librarian")
def is_member(user):
    return has_role(user, "Member")


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class RegisterView(CreateView): 
    form_class = UserCreationForm()
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class ProfileView(TemplateView):
    template_name = 'relationship_app/profile.html'
    # user = self.get_object
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # user = self.get_object()
        context["user"] = self.request.user
        return context
    
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login

class loginPage(LoginView):
    template_name = 'relationship_app/login.html'

class logoutPage(LogoutView):
    template_name = 'relationship_app/logout.html'

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-books')
    else:
        form = BookForm()
>>>>>>> eda9e73fc087c860423e0890d9594b1957ff7793
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('list-books')
<<<<<<< HEAD
=======
=======
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list-books')
    else:
        form = BookForm(instance=book)
>>>>>>> eda9e73fc087c860423e0890d9594b1957ff7793
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list-books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef

# ─── Library Detail ──────────────────────────────────────────
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.get_object().books.all()
        return context

# ─── Role-Based Views ────────────────────────────────────────
def has_role(user, role):
    return UserProfile.objects.filter(user=user, role=role).exists()

@user_passes_test(lambda u: has_role(u, "Admin"))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: has_role(u, "Librarian"))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: has_role(u, "Member"))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# ─── Auth & Profile ──────────────────────────────────────────
class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class ProfileView(TemplateView):
    template_name = 'relationship_app/profile.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

class LoginPage(LoginView):
    template_name = 'relationship_app/login.html'

class LogoutPage(LogoutView):
    template_name = 'relationship_app/logout.html'

# ─── Home Redirect ───────────────────────────────────────────
@login_required(login_url='login')
def home_redirect(request):
<<<<<<< HEAD
    return redirect('list-books')
=======
    return redirect('list-books')
=======
# class MemberView(TemplateView):
>>>>>>> eda9e73fc087c860423e0890d9594b1957ff7793
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef
