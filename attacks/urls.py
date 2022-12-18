from django.urls import path

from . import views

urlpatterns = [
    path('', views.attacks, name='attacks'),
    path('<int:attack_id>/', views.attack, name='attack'),
    path('new_attack/', views.new_attack, name='new_attack'),
    path('<int:attack_id>/start', views.start_attack, name='start_attack'),
    path('<int:attack_id>/finish', views.finish_attack, name='finish_attack'),
    path('stop', views.stop_attacks, name='stop_attacks'),
]