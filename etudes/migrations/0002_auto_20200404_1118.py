# Generated by Django 3.0.5 on 2020-04-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudes',
            name='description',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='etudes',
            name='duree',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='etudes',
            name='ects',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='etudes',
            name='objectif',
            field=models.TextField(max_length=1000),
        ),
    ]
