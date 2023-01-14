from rest_framework import serializers
from .models import *
 
class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('id', 'word', 'meaning_capitalized', 'meaning', 'romaji') 

class HiraganaSerializer(serializers.ModelSerializer):
    ex = ExampleSerializer(many=True, read_only=False)
    sound = serializers.FileField(source='vowel.sound')
    vowel = serializers.CharField(source='vowel.vowel')

    class Meta:
        model = Hiragana
        fields = '__all__'


class KatakanaSerializer(serializers.ModelSerializer):
    ex = ExampleSerializer(many=True, read_only=False)
    sound = serializers.FileField(source='vowel.sound')
    vowel = serializers.CharField(source='vowel.vowel')

    class Meta:
        model = Katakana
        fields = '__all__'


class VowelSerializer(serializers.ModelSerializer):
    hiragana_char = serializers.CharField(source='hiragana.hiragana')
    katakana_char = serializers.CharField(source='katakana.katakana')

    class Meta:

        model = Vowel
        fields = (
            'vowel',
            'hiragana_char',
            'katakana_char',
            'sound',
            'hiragana',
        )
        depth = 5

class KanaTypeSerializer(serializers.ModelSerializer):
    hiragana = serializers.SerializerMethodField()
    katakana = KatakanaSerializer(many=True, read_only=True)
    
    def get_hiragana(self, instance):
        hiragana = instance.hiragana.all().order_by('hiragana')
        return HiraganaSerializer(hiragana, many=True, read_only=True).data

    class Meta:
        model = KanaType
        fields = ('id','kana_type', 'hiragana','katakana')
