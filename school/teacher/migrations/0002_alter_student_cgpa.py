# Generated by Django 4.2.5 on 2023-10-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cgpa',
            field=models.FloatField(),
        ),
    ]
