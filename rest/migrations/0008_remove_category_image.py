# Generated by Django 5.0.7 on 2024-08-06 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0007_alter_category_image_alter_menu_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
