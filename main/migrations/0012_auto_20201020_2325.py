# Generated by Django 3.0.6 on 2020-10-20 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerwall',
            name='secret',
            field=models.CharField(max_length=35, unique=True),
        ),
    ]