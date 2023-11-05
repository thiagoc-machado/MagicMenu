# Generated by Django 4.2.5 on 2023-09-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('age', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('date_cad', models.DateField()),
                ('date_upd', models.DateField()),
                ('date_del', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('notes', models.TextField()),
            ],
        ),
    ]