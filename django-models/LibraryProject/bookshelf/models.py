from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

<<<<<<< HEAD


=======
>>>>>>> eda9e73fc087c860423e0890d9594b1957ff7793
# Create your models here.

