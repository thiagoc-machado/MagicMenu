# Generated by Django 4.2.5 on 2023-10-10 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_menu_nutrition_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='deleted_by',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='updated_by',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
