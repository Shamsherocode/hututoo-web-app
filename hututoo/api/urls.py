from .views import ListUsers
from django.urls import path
# from . import views

urlpatterns = [
    path('', ListUsers.as_view()),
]