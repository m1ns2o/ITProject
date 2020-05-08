from django.urls import path
from sruser import views

urlpatterns = [
    path('register/', views.register),
]
