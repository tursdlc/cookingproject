from django.db import models
from users_app.models import User


# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    time = models.IntegerField(default=0, help_text="Total time in seconds for the recipe")

    def __str__(self):
        return f'Recipe: {self.title}'
