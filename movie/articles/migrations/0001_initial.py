# Generated by Django 3.2.8 on 2021-11-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('intro', models.CharField(max_length=250, verbose_name='intro')),
                ('full_text', models.TextField(verbose_name='article')),
                ('date', models.DateTimeField(verbose_name='public')),
            ],
        ),
    ]
