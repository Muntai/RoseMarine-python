# Generated by Django 4.1.7 on 2023-03-12 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuhnya', '0004_remove_category_category_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
