# Generated by Django 3.2.8 on 2022-05-21 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='precio',
            field=models.IntegerField(default=9999),
            preserve_default=False,
        ),
    ]
