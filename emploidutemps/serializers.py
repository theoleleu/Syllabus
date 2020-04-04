
from emploidutemps.models import Emploidutemps
from rest_framework import serializers

class EmploidutempsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emploidutemps
        fields = ('nomducours', 'enseignant','horaire', 'salle')