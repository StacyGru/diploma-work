# Generated by Django 4.1.7 on 2023-05-31 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_status_alter_order_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketitem',
            name='ordered',
            field=models.IntegerField(default=False),
        ),
    ]
