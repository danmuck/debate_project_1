# Generated by Django 2.1.5 on 2021-09-25 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debate_project', '0002_auto_20210925_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidence',
            name='speaker',
            field=models.CharField(default='n/a', max_length=50, null=True),
        ),
    ]
