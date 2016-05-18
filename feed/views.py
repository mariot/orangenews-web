from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import ActualiteSerializer, DepecheSerializer

from .models import Actualite, Depeche

def home(request):
	return redirect('/feed/')

class ActualiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Actualite.objects.all().order_by('-date')
    serializer_class = ActualiteSerializer


class DepecheViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Depeche.objects.all().order_by('-heure')
    serializer_class = DepecheSerializer