# Generated by Django 3.2.7 on 2021-09-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210923_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default='n/a'),
        ),
    ]
