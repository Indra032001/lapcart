# Generated by Django 5.0.2 on 2024-02-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=20)),
                ('processor', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('rom', models.IntegerField()),
                ('ram', models.IntegerField()),
            ],
        ),
    ]
