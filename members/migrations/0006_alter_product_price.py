# Generated by Django 5.0.1 on 2024-01-27 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_product_date_of_publish_alter_product_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]
