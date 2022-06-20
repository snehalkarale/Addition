from django.contrib import admin
from django.urls import path
from Add.views import add

urlpatterns = [
    path('hello/', add.as_view(),name='add'),
]
