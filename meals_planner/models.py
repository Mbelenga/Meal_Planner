from django.db import models

class Meal(models.Model):
    """Different kind of meals and also planning part"""
    name = models.CharField(max_length=100)
    """
    This creates a column in the table called name. 
    It's a text field limited to 100 characters. 
    CharField is used for short strings.
    """
    calories = models.IntegerField()
    is_vegetarian = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)

class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cooking_Time = models.IntegerField()
    servings = models.IntegerField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.name