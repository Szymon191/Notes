from django.db import models
from django.db.models import Model
from django.utils import timezone


class Categorie(models.Model):
    title        = models.CharField(max_length=80)
    icon         = models.CharField(max_length=80)
    bg_color     = models.CharField(max_length=15)

    cateManager = models.Manager()

    def __str__(self):
        return self.title


class Note(models.Model):
    title        = models.CharField(max_length=250)
    publish_date = models.DateField(default=timezone.now)
    body         = models.TextField(max_length=2500)
    categorie    = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='kategoria', )

    noteManager = models.Manager()