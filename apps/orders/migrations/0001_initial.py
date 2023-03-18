# Generated by Django 4.1.7 on 2023-03-18 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reg_and_auth', '0001_initial'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reg_and_auth.user')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.product')),
            ],
            options={
                'db_table': 'basket_item',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('building_number', models.CharField(max_length=5)),
                ('entrance_number', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('apartment_number', models.CharField(max_length=5)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reg_and_auth.user')),
            ],
            options={
                'db_table': 'delivery_address',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date_and_time', models.DateTimeField()),
                ('delivery_date_and_time', models.DateTimeField()),
                ('sum', models.IntegerField()),
                ('status', models.CharField(choices=[('в обработке', 'в обработке'), ('в сборке', 'в сборке'), ('в доставке', 'в доставке'), ('выполнен', 'выполнен'), ('отменён', 'отменён')], max_length=150)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reg_and_auth.user')),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.deliveryaddress')),
            ],
            options={
                'db_table': 'order',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket_item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.basketitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.order')),
            ],
            options={
                'db_table': 'order_item',
                'managed': True,
            },
        ),
    ]
