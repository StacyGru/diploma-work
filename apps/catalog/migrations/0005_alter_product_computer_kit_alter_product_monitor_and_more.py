# Generated by Django 4.1.7 on 2023-04-27 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_computer_kit_alter_product_monitor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='computer_kit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.computerkitdetails'),
        ),
        migrations.AlterField(
            model_name='product',
            name='monitor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.monitordetails'),
        ),
        migrations.AlterField(
            model_name='product',
            name='system_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.systemunitfilters'),
        ),
    ]
