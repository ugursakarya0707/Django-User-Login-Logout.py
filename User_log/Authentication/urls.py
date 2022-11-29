from django.urls import path
from .views import on_sayfa

urlpatterns = [
    path('', on_sayfa, name="on_sayfa")
]