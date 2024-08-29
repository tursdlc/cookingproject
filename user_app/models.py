from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"