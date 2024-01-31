"""
    Jordyn Kuhn
    CIS 218
    1/30/2024
"""

from django.views.generic import ListView
from .models import Todo

class HomePageView(ListView):
    """Home Page View"""

    model = Todo
    template_name = "home.html"