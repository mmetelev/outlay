# Generated by Django 4.1.2 on 2022-11-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spgz',
            name='spgz_name',
            field=models.CharField(max_length=300),
        ),
    ]