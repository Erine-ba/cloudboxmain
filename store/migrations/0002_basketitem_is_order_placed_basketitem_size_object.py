# Generated by Django 5.0.1 on 2024-02-28 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketitem',
            name='is_order_placed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basketitem',
            name='size_object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.size'),
        ),
    ]
