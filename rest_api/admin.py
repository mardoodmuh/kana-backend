from django.contrib import admin
from .models import * 

# Register your models here.
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('word','meaning')
    def get_queryset(self, request):
        queryset = super(ExampleAdmin, self).get_queryset(request)
        queryset = queryset.order_by('word')
        return queryset

admin.site.register(Vowel)
admin.site.register(Hiragana)
admin.site.register(Katakana)
admin.site.register(Example, ExampleAdmin)
admin.site.register(KanaType)
