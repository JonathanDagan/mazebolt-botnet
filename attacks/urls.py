from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_attack/', views.new_attack, name='new_attack'),
    path('stop', views.stop_attacks, name='stop_attacks'),
]