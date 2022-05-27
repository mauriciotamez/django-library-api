from django.db import models
import uuid
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_id = models.UUIDField(default=uuid.uuid4, max_length=36)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date_of_publication = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
