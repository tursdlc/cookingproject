from django.test import TestCase, Client
from .models import Recipe
# Create your tests here.

class RecipeTestCase(TestCase):
    def setUp(self):

        # Create recipes
        a1 = Recipe.objects.create(title= "Almond milk", description= "add ingredients", time= 90)


