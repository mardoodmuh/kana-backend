# Generated by Django 4.1.3 on 2022-12-28 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0011_katakana_kana_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='KanaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kana_type', models.CharField(choices=[('gojuuon', 'gojuuon'), ('dakuon', 'dakuon'), ('handakuon', 'handakuon'), ('youon', 'youon'), ('sokuon', 'sokuon')], default='gojuuon', max_length=32, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='hiragana',
            name='kana_type',
        ),
        migrations.RemoveField(
            model_name='katakana',
            name='kana_type',
        ),
        migrations.AlterField(
            model_name='hiragana',
            name='ex',
            field=models.ManyToManyField(blank=True, default=None, to='rest_api.example'),
        ),
        migrations.AlterField(
            model_name='katakana',
            name='ex',
            field=models.ManyToManyField(blank=True, default=None, to='rest_api.example'),
        ),
    ]
