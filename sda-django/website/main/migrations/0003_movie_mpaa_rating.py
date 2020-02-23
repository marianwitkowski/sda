# Generated by Django 3.0.3 on 2020-02-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200223_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='mpaa_rating',
            field=models.CharField(choices=[('-', 'Brak'), ('G', 'Rating G'), ('PG-13', 'Rating PG-13'), ('NC-17', 'Rating NC-17')], default=1, max_length=5),
        ),
    ]
