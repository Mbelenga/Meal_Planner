from django.urls import path
from . import views

app_name = 'meals_planner'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Mealplans Page
    path('mealplans/', views.mealplans_list, name='mealplans_list'),

    # Forms page 
    path('mealplans/new/', views.create_mealplan, name='create_mealplan'),
]