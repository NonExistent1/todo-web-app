"""
    Jordyn Kuhn
    CIS 218
    1/30/2024
"""

from django.urls import path
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home")
]
