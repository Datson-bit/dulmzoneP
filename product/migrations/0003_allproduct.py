# Generated by Django 3.1.4 on 2021-01-06 08:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_delete_allproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('price', models.FloatField()),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
