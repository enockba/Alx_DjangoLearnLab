from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    # ─── Book Management ─────────────────────────────────────
    path('books/', views.list_books, name='list-books'),
    path('add_book/', views.add_book, name='add-book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit-book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete-book'),

    # ─── Library ─────────────────────────────────────────────
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),

    # ─── Role-Based Access ───────────────────────────────────
    path('admin/', views.admin_view, name='admin-view'),
    path('librarian/', views.librarian_view, name='librarian-view'),
    path('member/', views.member_view, name='member-view'),

    # ─── Auth & Profile ──────────────────────────────────────
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', views.LogoutPage.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    # ─── Home ────────────────────────────────────────────────
    path('', views.home_redirect, name='home'),
]
=======
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import RegisterView
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
 
    path('register/', RegisterView.as_view(), name='register'),

    path('register/', views.register, name='register'), 

    path('admin/', views.admin_view, name='admin_view'),

    path('librarian/', views.librarian_view, name='librarian_view'),

    path('member/', views.member_view, name='member_view'),

    path("add/", views.add_book, name="add_book"),

    path("edit/<int:book_id>/", views.edit_book, name="edit_book"),

     path("delete/<int:book_id>/", views.delete_book, name="delete_book"),

    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('booklist/',views.booklist, name = "booklist"),
    
    path('', views.home_redirect, name='home'),
    
    path('add_book/', views.add_book, name='add-book'),
    
    path('edit_book/<int:pk>/', views.edit_book, name='edit-book'),
    
    path('delete_book/<int:pk>/', views.delete_book, name='delete-book'),
    
    path('books/', views.list_books, name='list-books'),  # existing view

     
]  
>>>>>>> eda9e73fc087c860423e0890d9594b1957ff7793
