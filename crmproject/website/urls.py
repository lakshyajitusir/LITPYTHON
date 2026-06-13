from django.urls import path
from . import views


urlpatterns = [

    path('', views.landing, name='landing'),

    path('register/', views.register, name='register'),

    path('home/', views.home, name='home'),

    path('create/', views.create_customer, name='create'),

    path('update/<int:pk>/', views.update_customer, name='update'),

    path('delete/<int:pk>/', views.delete_customer, name='delete'),

]