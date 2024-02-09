"""
    Jordyn Kuhn
    CIS 218
    1/30/2024
"""
from django.db import models

class Todo(models.Model):
    text = models.TextField()
    complete_by = models.DateTimeField()

    def __str__(self):
        """String method"""
        return self.text[:50]
