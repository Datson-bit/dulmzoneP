# Generated by Django 3.1.4 on 2021-01-13 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210108_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
        migrations.AddField(
            model_name='product',
            name='img_url',
            field=models.CharField(default='', max_length=2083),
        ),
    ]