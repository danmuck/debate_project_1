# Generated by Django 2.1.5 on 2021-09-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='subject',
            field=models.TextField(default=None),
        ),
    ]
