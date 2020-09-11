from django.urls import include, path
from . import views

urlpatterns = [
    path('create_voluntary/', views.create_voluntary, name='criar'),
    path('list_voluntary/', views.list_voluntary, name='lista-voluntario'),
]