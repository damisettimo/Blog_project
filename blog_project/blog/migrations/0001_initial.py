# Generated by Django 4.0.5 on 2022-06-26 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('subtitle', models.CharField(max_length=155)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(max_length=60000)),
            ],
        ),
    ]