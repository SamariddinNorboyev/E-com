# Generated by Django 5.1.4 on 2025-04-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default=1, upload_to='pictures'),
            preserve_default=False,
        ),
    ]
