# Generated by Django 3.1.4 on 2021-01-18 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]