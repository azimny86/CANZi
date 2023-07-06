from django.db import models

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

