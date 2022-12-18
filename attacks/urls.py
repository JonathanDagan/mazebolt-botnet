from django.urls import path

from . import views

urlpatterns = [
    path('', views.attacks, name='attacks'),
    path('<int:attack_id>/', views.attack, name='attack'),
    path('new_attack/', views.new_attack, name='new_attack'),
    path('stop', views.stop_attacks, name='stop_attacks'),
]