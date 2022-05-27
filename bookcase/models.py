# from unicodedata import name
from django.db import models
from book.models import Book
from core.models import User
import uuid

# Create your models here.

class Rack(models.Model):
    rack_id = models.UUIDField(default=uuid.uuid4,  max_length=36)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name    
class BookItem(models.Model):
    
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    current_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.book} | {self.rack} | {self.id}"
    
    