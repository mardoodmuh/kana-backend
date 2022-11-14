from django.db import models


class Example(models.Model):
    word = models.CharField(max_length=255)
    meaning = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.word


class Hiragana(models.Model):
    GOJUUON = 'gojuuon'
    DAKUON = 'dakuon'
    HANDAKOUN = 'handakuon'
    YOUON = "youon"
    SOKUON = "sokuon"
    hiragana = models.CharField(max_length=3)
    ex = models.ManyToManyField(Example, null=True, blank=True, default=None)
    TYPE = [
        (GOJUUON, ('gojuuon')),
        (DAKUON, ('dakuon')),
        (HANDAKOUN, ('handakuon')),
        (YOUON, ('youon')),
        (SOKUON, ('sokuon')),
    ]
    kana_type = models.CharField(
        max_length=32,
        choices=TYPE,
        null=True,
        default=None,
    )

    def __str__(self):
        return self.hiragana


class Katakana(models.Model):
    GOJUUON = 'gojuuon'
    DAKUON = 'dakuon'
    HANDAKOUN = 'handakuon'
    YOUON = "youon"
    SOKUON = "sokuon"
    katakana = models.CharField(max_length=3)
    ex = models.ManyToManyField(Example, null=True, blank=True, default=None)
    TYPE = [
        (GOJUUON, ('gojuuon')),
        (DAKUON, ('dakuon')),
        (HANDAKOUN, ('handakuon')),
        (YOUON, ('youon')),
        (SOKUON, ('sokuon')),
    ]
    kana_type = models.CharField(
        max_length=32,
        choices=TYPE,
        null=True,
        default=GOJUUON,
    )

    def __str__(self):
        return self.katakana


class Vowel(models.Model):
    vowel = models.CharField(max_length=3)
    hiragana = models.OneToOneField(
        Hiragana, default=None, on_delete=models.CASCADE)
    katakana = models.OneToOneField(
        Katakana, default=None, on_delete=models.CASCADE)
    sound = models.FileField(upload_to='sounds/', null=True, blank=True)

    def __str__(self):
        return self.vowel
