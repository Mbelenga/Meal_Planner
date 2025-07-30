from django.shortcuts import render
from .models import MealPlan

def index(request):
    """ A simple Home Page for the Meal Planner """
    return render(request, 'meals_planner/index.html')

def mealplans_list(request):
    mealplans = MealPlan.objects.all  #Fetch all mealplan objects
    return render(request, 'meals_planner/mealplans_list.html', {'mealplans':mealplans})