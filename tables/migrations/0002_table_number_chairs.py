# Generated by Django 4.2.5 on 2023-09-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='number_chairs',
            field=models.IntegerField(null=True),
        ),
    ]
