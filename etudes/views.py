from django.shortcuts import render

from rest_framework import viewsets
from etudes.models import Etudes
from etudes.serializers import EtudesSerializer

class EtudesViewSet(viewsets.ModelViewSet):
    queryset = Etudes.objects.all()
    serializer_class = EtudesSerializer