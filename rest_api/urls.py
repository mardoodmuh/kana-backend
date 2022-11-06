from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('vowels', views.VowelsView)
router.register('hiragana', views.HiraganaView)
router.register('katakana', views.KatakanaView)

urlpatterns = [
        path('', include(router.urls)),
        path('home/', views.html_view)
    ]
