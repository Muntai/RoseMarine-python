# Generated by Django 4.1.7 on 2023-03-12 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuhnya', '0002_rename_menuitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]