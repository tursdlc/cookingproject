from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.TextField()


    def __str__(self):
        return f'Recipe: {self.name}'