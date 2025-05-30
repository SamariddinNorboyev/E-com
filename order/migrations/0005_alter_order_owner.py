# Generated by Django 5.1.4 on 2025-04-06 17:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_owner_alter_order_product_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner_orders', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
