from django.shortcuts import render
from .models import MealPlan
from .forms import MealPlanForm

def index(request):
    """ A simple Home Page for the Meal Planner """
    return render(request, 'meals_planner/index.html')

def mealplans_list(request):
    mealplans = MealPlan.objects.all  #Fetch all mealplan objects
    return render(request, 'meals_planner/mealplans_list.html', {'mealplans': mealplans})

def create_mealplan(request):
    if request.method == 'POST':
        form = MealPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meals_planner:mealplans_list')
    else:
        form = MealPlanForm()
    
    return render(request, 'meals_planner/createmealplan.html', {'form': form})

def add_mealplan(request):
    if request.method == 'POST':
        form = MealPlanForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('mealplans_list')
    else:
        form = MealPlanForm()
    return render(request, 'meals_planner/add_mealplan.html', {'form': form})