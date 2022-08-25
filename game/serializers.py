from rest_framework import serializers
from .models import *

class Face_readerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Face_reader
        fields='__all__'

class Speech_to_TextSerializer(serializers.ModelSerializer):
    class Meta:
        model=Speech_to_Text
        fields='__all__'

class Text_readerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Text_reader
        fields='__all__'


class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Scene
        fields='__all__'

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Character
        fields='__all__'
class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fact
        fields='__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'

class Scene_pictureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Scene_picture
        fields='__all__'

class Scene_textSerializer(serializers.ModelSerializer):
    class Meta:
        model=Scene_text
        fields='__all__'

class Question_AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Character
        fields='__all__'

class DivergesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Character
        fields='__all__'
