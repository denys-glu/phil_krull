from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('name/<str:user_name>', views.say_hi),
    path('process', views.handle_form)
]