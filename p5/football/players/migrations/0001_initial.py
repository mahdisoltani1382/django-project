# Generated by Django 3.2.8 on 2021-11-13 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=128)),
                ('post', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
    ]
