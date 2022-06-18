from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.Index , name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
]