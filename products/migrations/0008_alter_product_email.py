# Generated by Django 5.1.7 on 2025-03-09 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='email',
            field=models.EmailField(default='test/@gnail.com', max_length=254),
        ),
    ]
