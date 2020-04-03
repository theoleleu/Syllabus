from etudes.models import Etudes
from rest_framework import serializers

class EtudesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Etudes
        fields = ('cours', 'enseignant', 'duree', 'ects', 'prerequis', 'objectif', 'description', 'evaluation')
