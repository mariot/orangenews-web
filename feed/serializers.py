from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Actualite, Depeche


class ActualiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actualite
        #fields = ('url', 'username', 'email', 'groups')


class DepecheSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Depeche
        #fields = ('url', 'name')