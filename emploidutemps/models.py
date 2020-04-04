from django.db import models

class Emploidutemps(models.Model):
    nomducours = models.CharField(max_length=100)
    enseignant = models.CharField(max_length=100)
    horaire = models.DateTimeField()
    salle = models.CharField(max_length=80)

    def __str__(self):
        return self.nom