from django.db import models

# Create your models here.
class LibraryBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    available = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    class Meta():
        ordering = ['author']