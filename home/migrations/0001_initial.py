# Generated by Django 4.0.1 on 2022-01-15 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('manfacture_date', models.DateField()),
                ('fruits_description', models.TextField()),
                ('is_fresh', models.BooleanField(default=True)),
            ],
        ),
    ]
