from django.db import models



# Create your models here.
class Recipes(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    time = models.IntegerField(default=0, help_text="Total time in seconds for the recipe")

    def __str__(self):
        return f'Recipe: {self.title}'
