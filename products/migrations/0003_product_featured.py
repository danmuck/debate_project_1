# Generated by Django 2.1.5 on 2021-09-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210919_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
