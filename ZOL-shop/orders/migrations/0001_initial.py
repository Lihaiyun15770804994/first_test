# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-10 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='用户id')),
                ('order_code', models.CharField(max_length=100, verbose_name='订单编号')),
                ('total_count', models.IntegerField(verbose_name='订单总数量')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='总金额')),
                ('status', models.SmallIntegerField(verbose_name='1 未支付,2未发货,3未收货')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='用户id')),
                ('order_code', models.CharField(max_length=100, verbose_name='订单编号')),
                ('goods_id', models.IntegerField(verbose_name='商品id')),
                ('counts', models.IntegerField(verbose_name='商品数量')),
                ('price', models.DecimalField(decimal_places=3, max_digits=9, verbose_name='价格')),
            ],
            options={
                'db_table': 'order_detail',
            },
        ),
    ]
