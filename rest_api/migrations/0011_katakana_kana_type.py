# Generated by Django 4.1.3 on 2022-11-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0010_remove_katakana_kana_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='katakana',
            name='kana_type',
            field=models.CharField(choices=[('gojuuon', 'gojuuon'), ('dakuon', 'dakuon'), ('handakuon', 'handakuon'), ('youon', 'youon'), ('sokuon', 'sokuon')], default='gojuuon', max_length=32, null=True),
        ),
    ]
