# Generated by Django 4.2.5 on 2023-10-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
