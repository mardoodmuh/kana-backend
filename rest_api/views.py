from django.shortcuts import render
from kana.settings import BASE_DIR
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, viewsets

# Create your views here.


class VowelsView(viewsets.ModelViewSet):
    queryset = Vowel.objects.all()
    serializer_class = VowelSerializer

    def filter_queryset(self, queryset):
        queryset = super(VowelsView, self).filter_queryset(queryset)
        return queryset.order_by("vowel")


class HiraganaView(viewsets.ModelViewSet):
    queryset = Hiragana.objects.all()
    serializer_class = HiraganaSerializer

    def filter_queryset(self, queryset):
        queryset = super(HiraganaView, self).filter_queryset(queryset)
        return queryset.order_by("hiragana")


class KatakanaView(viewsets.ModelViewSet):
    queryset = Katakana.objects.all()
    serializer_class = KatakanaSerializer

    def filter_queryset(self, queryset):
        queryset = super(KatakanaView, self).filter_queryset(queryset)
        return queryset.order_by("katakana")


class ExampleView(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer

    def filter_queryset(self, queryset):
        queryset = super(ExampleView, self).filter_queryset(queryset)
        return queryset.order_by("word")


def html_view(request):
    vowels = Vowel.objects.all()
    context = {
        'vowels': vowels,
    }
    return render(request, 'home.html', context=context)
