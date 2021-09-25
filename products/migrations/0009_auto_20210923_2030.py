# Generated by Django 3.2.7 on 2021-09-23 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='email',
            field=models.EmailField(default='n/a', max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
