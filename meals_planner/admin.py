from django.contrib import admin

from .models import Meal, Ingredient, MealPlan, Recipe

admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(MealPlan)
admin.site.register(Recipe)