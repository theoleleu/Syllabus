from django.shortcuts import render
from rest_framework import viewsets
from emploidutemps.models import Emploidutemps
from emploidutemps.serializers import EmploidutempsSerializer

class EmploidutempsViewSet(viewsets.ModelViewSet):
    queryset = Emploidutemps.objects.all()
    serializer_class = EmploidutempsSerializer