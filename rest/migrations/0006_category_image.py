# Generated by Django 5.0.7 on 2024-08-05 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_menu_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
