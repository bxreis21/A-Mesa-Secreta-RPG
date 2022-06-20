from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ficha/<int:pk>', views.ficha, name='ficha'),
    path('mesa/<int:pk>', views.mesa, name='mesa'),
]