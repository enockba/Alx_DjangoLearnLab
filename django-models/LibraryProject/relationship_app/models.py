<<<<<<< HEAD
=======
<<<<<<< HEAD
=======

>>>>>>> eda9e73fc087c860423e0890d9594b1957ff7793
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

<<<<<<< HEAD
# ─── Core Models ─────────────────────────────────────────────
class Author(models.Model):
    name = models.CharField(max_length=100)
=======
<<<<<<< HEAD
# ─── Core Models ─────────────────────────────────────────────
class Author(models.Model):
    name = models.CharField(max_length=100)
=======

class Author(models.Model):
    name = models.CharField(max_length=100)

>>>>>>> eda9e73fc087c860423e0890d9594b1957ff7793
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
<<<<<<< HEAD
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
=======
<<<<<<< HEAD
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
=======
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
class Meta:
>>>>>>> eda9e73fc087c860423e0890d9594b1957ff7793
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
<<<<<<< HEAD

    def __str__(self):
=======
<<<<<<< HEAD

    def __str__(self):
=======
def __str__(self):
>>>>>>> eda9e73fc087c860423e0890d9594b1957ff7793
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======

>>>>>>> eda9e73fc087c860423e0890d9594b1957ff7793
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef
    def __str__(self):
        return self.name

# ─── User Role Extension ─────────────────────────────────────
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
<<<<<<< HEAD
        UserProfile.objects.create(user=instance)
=======
        UserProfile.objects.create(user=instance)
=======

    def __str__(self):
        return self.name
    
    class UserProfile(models.Model):
      ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
     if created:
         UserProfile.objects.create(user=instance)


# Create your models here.
>>>>>>> eda9e73fc087c860423e0890d9594b1957ff7793
>>>>>>> 551691cb27b10bdeb2ae796c14459d19acbfefef
