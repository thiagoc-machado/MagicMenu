# Generated by Django 4.2.5 on 2023-10-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_menu_ingredients_delete_menu_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='nutrition_grade',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]