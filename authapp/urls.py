from django.urls import path
from .views import home

urlpatterns = [
    path("greetings/<str:greet>", home, name='')
]
