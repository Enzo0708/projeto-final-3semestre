# Generated by Django 5.0.6 on 2024-05-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Senai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=1500)),
                ('logo', models.ImageField(upload_to='logo/')),
            ],
        ),
    ]
