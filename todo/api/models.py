from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    