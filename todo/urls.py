from django.urls import path

from .views import home, remover

urlpatterns = [
    path('',home,name='home'),
    path('<str:whom>/',remover,name='remover')
]