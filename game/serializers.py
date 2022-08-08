from rest_framework import serializers
from .models import *

class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Scene
        fields='__all__'

