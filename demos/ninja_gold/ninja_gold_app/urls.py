from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process/<str:building>', views.process_form),
    path('reset', views.reset)
]