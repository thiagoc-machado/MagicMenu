# Generated by Django 4.2.5 on 2023-10-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_alter_client_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='zip',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
