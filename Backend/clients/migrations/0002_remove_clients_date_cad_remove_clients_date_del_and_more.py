# Generated by Django 4.2.5 on 2023-09-30 07:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='date_cad',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='date_del',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='date_upd',
        ),
        migrations.AddField(
            model_name='clients',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clients',
            name='created_by',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='deleted_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='deleted_by',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='photo',
            field=models.ImageField(null=True, upload_to='clients'),
        ),
        migrations.AddField(
            model_name='clients',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='updated_by',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='zip',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='age',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]