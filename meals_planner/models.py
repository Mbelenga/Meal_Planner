from django.db import models

class Meals(models.Model):
    """Different kind of meals and also planning part"""
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    is_vegetarian = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name