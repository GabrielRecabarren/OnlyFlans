# Generated by Django 3.2.4 on 2024-06-05 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20240605_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flan',
            name='rating',
        ),
    ]