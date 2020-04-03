from django.db import models

class Etudes(models.Model):
    cours = models.CharField(max_length=300)
    enseignant = models.CharField(max_length=300)
    duree = models.CharField(max_length=50)
    ects = models.FloatField()
    prerequis = models.CharField(max_length=30)
    objectif = models.TextField(max_length=1000)
    description = models.TextField(max_length=100000)
    evaluation = models.CharField(max_length=200)
   
    def __str__(self):
        return self.nom