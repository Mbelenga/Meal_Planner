from django.shortcuts import render

def index(request):
    """ A simple Home Page for the Meal Planner """
    return render(request, 'meals_planner/index.html')
