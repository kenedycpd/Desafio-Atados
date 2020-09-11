from django.urls import include, path
from . import views

urlpatterns = [
    path('create_actions/', views.create_actions, name='criar_acoes'),
    path('list_actions/', views.list_actions, name='lista-acoes'),
]