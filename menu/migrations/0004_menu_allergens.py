# Generated by Django 4.2.5 on 2023-09-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menu_allergen_menu_gluten_menu_lactose_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='allergens',
            field=models.TextField(null=True),
        ),
    ]
