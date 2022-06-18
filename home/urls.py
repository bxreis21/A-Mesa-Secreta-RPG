from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.Index , name='index'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
]