# Generated by Django 4.2.5 on 2023-10-20 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_alter_client_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
