# Generated by Django 3.2 on 2023-06-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YuMetrics_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='definition',
            field=models.CharField(max_length=255, unique=True, verbose_name='Metric definition'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Metric name'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='transcript',
            field=models.CharField(max_length=50, unique=True, verbose_name='Metric name transcript'),
        ),
    ]
