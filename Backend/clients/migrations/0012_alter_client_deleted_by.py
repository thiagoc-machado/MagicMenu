# Generated by Django 4.2.5 on 2023-10-27 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_alter_client_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='deleted_by',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]