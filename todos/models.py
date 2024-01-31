from django.db import models

class Todo(models.Model):
    text = models.TextField()

    def __str__(self):
        """String method"""
        return self.text[:50]
