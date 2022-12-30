from django.db import models


class Example(models.Model):
    word = models.CharField(max_length=255)
    meaning = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.word

class Hiragana(models.Model):
    hiragana = models.CharField(max_length=3)
    ex = models.ManyToManyField(Example, blank=True, default=None) 

    def __str__(self):
        return self.hiragana


class Katakana(models.Model):
    katakana = models.CharField(max_length=3)
    ex = models.ManyToManyField(Example, blank=True, default=None)
    # kanatype = models.ForeignKey(KanaType, blank=True, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.katakana

class KanaType(models.Model):
    GOJUUON = 'Gojuuon'
    DAKUON = 'Dakuon'
    HANDAKOUN = 'Handakuon'
    YOUON = "Youon"
    SOKUON = "Sokuon"
    TYPE = [
        (GOJUUON, ('Gojuuon')),
        (DAKUON, ('Dakuon')),
        (HANDAKOUN, ('Handakuon')),
        (YOUON, ('Youon')),
        (SOKUON, ('Sokuon')),
    ]
    kana_type = models.CharField(
        max_length=32,
        choices=TYPE,
        null=True,
        default=GOJUUON,
    )
    hiragana = models.ManyToManyField(
        Hiragana, default=None)
    katakana = models.ManyToManyField(
        Katakana, default=None) 

    def __str__(self):
        return self.kana_type

class Vowel(models.Model):
    vowel = models.CharField(max_length=3)
    hiragana = models.OneToOneField(
        Hiragana, default=None, on_delete=models.CASCADE)
    katakana = models.OneToOneField(
        Katakana, default=None, on_delete=models.CASCADE)
    sound = models.FileField(upload_to='sounds/', null=True, blank=True)

    def __str__(self):
        return self.vowel
