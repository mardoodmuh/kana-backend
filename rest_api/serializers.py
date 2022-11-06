from rest_framework import serializers
from .models import *

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example 
        fields = '__all__'

class HiraganaSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Hiragana
        fields = '__all__' 

class KatakanaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Katakana 
        fields = ('katakana',)

class VowelSerializer(serializers.HyperlinkedModelSerializer):
    hiragana_char = serializers.CharField(source='hiragana.hiragana')
    katakana_char = serializers.CharField(source='katakana.katakana')

    class Meta:

        model = Vowel 
        fields = ('vowel', 'hiragana_char', 'katakana_char', 'sound' ) 
