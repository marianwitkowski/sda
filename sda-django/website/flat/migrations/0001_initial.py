# Generated by Django 3.0.3 on 2020-02-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('url', models.TextField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('rooms', models.PositiveSmallIntegerField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('price_m2', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('area', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('district', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Mieszkanie',
                'verbose_name_plural': 'Mieszkania',
            },
        ),
    ]
