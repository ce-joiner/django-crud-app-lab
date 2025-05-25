from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'), 
     path('teas/', views.tea_index, name='tea_index'),
     path('teas/<int:tea_id>/', views.tea_detail, name='tea-detail'),
     path('teas/create/', views.TeaCreate.as_view(), name='tea_create'),
     path('teas/<int:pk>/update/', views.TeaUpdate.as_view(), name='tea_update'),
     path('teas/<int:pk>/delete/', views.TeaDelete.as_view(), name='tea_delete'),
]

