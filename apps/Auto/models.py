# auto/models.py

from django.db import models

class Auto(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    user = models.ForeignKey()

    def __str__(self):
        return self.title
