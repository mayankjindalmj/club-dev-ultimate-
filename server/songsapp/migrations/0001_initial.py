# Generated by Django 3.0.6 on 2020-05-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=30)),
                ('song_artist', models.CharField(max_length=30)),
                ('song_genre', models.CharField(max_length=30)),
            ],
        ),
    ]