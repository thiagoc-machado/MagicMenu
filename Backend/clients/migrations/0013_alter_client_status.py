# Generated by Django 4.2.5 on 2023-10-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0012_alter_client_deleted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
