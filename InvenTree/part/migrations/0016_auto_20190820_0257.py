# Generated by Django 2.2.4 on 2019-08-20 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0015_auto_20190820_0251'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='partparameter',
            unique_together={('part', 'template')},
        ),
    ]
