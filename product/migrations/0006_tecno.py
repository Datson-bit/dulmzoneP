# Generated by Django 3.1.4 on 2021-01-06 23:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210106_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('price', models.FloatField()),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
