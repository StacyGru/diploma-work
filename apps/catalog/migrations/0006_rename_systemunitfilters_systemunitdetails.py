# Generated by Django 4.1.7 on 2023-06-20 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_monitordetails_connectors_delete_connectors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SystemUnitFilters',
            new_name='SystemUnitDetails',
        ),
    ]
