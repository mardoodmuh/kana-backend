# Generated by Django 4.0 on 2022-10-31 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_vowel_sound'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='hiragana',
            name='ex',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='rest_api.Example'),
        ),
    ]
