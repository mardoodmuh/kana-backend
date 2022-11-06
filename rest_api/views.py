from django.shortcuts import render
from kana.settings import BASE_DIR
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response 
from rest_framework import status, viewsets

# Create your views here.
@api_view(["GET", "POST"])
def home(request):
    vowel = Katakana.objects.all()
    if request.method == "GET":
        serializer = KatakanaSerializer(vowel, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = KatakanaSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data) 

@api_view(['GET', 'POST'])
def hiragana(request):
    hiragana = Hiragana.objects.all()
    if request.method == 'GET':
        serializer = HiraganaSerializer(hiragana, many=True)
    
    elif request.method == "POST":
        serializer = HiraganaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.data)

class VowelsView(viewsets.ModelViewSet):
    queryset = Vowel.objects.all()
    many=True
    serializer_class = VowelSerializer

class HiraganaView(viewsets.ModelViewSet):
    queryset = Hiragana.objects.all()
    serializer_class = HiraganaSerializer

class KatakanaView(viewsets.ModelViewSet):
    queryset = Katakana.objects.all()
    serializer_class = KatakanaSerializer

def html_view(request):
    vowels = Vowel.objects.all()
    context = {
            'vowels': vowels,
            }
    return render(request, 'home.html', context=context)
