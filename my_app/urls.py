from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'), 
     path('teas/', views.tea_index, name='tea_index'),
]