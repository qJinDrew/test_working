from django.urls import path
from . import views

urlpatterns = [
    path('', views.short, name='short'),
    path('index/', views.index, name='index')
]
