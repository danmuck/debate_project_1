# Generated by Django 2.1.5 on 2021-09-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('subject', models.TextField(null=True)),
                ('blogpost', models.TextField()),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
        ),
    ]
