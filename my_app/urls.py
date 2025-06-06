from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
     path('', views.Home.as_view(), name='home'),
     path('about/', views.about, name='about'), 
     path('teas/', views.tea_index, name='tea_index'),
     path('teas/<int:tea_id>/', views.tea_detail, name='tea-detail'),
     path('teas/create/', views.TeaCreate.as_view(), name='tea_create'),
     path('teas/<int:pk>/update/', views.TeaUpdate.as_view(), name='tea_update'),
     path('teas/<int:pk>/delete/', views.TeaDelete.as_view(), name='tea_delete'),
     path('teas/<int:tea_id>/brewing/', views.add_brewing, name='add-brewing'),
     path('teaware/create', views.TeawareCreate.as_view(), name='teaware_create'),
     path('teaware/<int:pk>/', views.TeawareDetail.as_view(), name='teaware_detail'),
     path('teaware/', views.TeawareList.as_view(), name='teaware-index'),
     path('teaware/<int:pk>/update/', views.TeawareUpdate.as_view(), name='teaware_update'),
     path('teaware/<int:pk>/delete/', views.TeawareDelete.as_view(), name='teaware_delete'),
     path('tea/<int:tea_id>/associate-teaware/<int:teaware_id>/', views.associate_teaware, name='associate-teaware'),
     path('teas/<int:tea_id>/remove-teaware/<int:teaware_id>/', views.remove_teaware, name='remove-teaware'),
     path('accounts/signup/', views.signup, name='signup'),

]

