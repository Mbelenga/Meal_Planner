from django.urls import path
from . import views

appname = 'meals_planner'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
]
urlpatterns = [
    path('mealplans/', views.mealplans_list, name='mealplans_list')
]