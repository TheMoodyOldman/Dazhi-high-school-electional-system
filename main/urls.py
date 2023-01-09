from django.urls import path
from .views import *

urlpatterns = [
    path('', ListElections.as_view(), name='mainpage')
]