# Generated by Django 4.1.4 on 2022-12-26 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('image', models.ImageField(upload_to='./static/image')),
                ('price', models.IntegerField(default=0, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='Gagarina street, 55', max_length=40)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_time', models.TimeField(default=django.utils.timezone.now)),
                ('to_time', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('item', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='order.item')),
                ('order', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_time', to='order.time'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ManyToManyField(through='order.OrderedItem', to='order.order'),
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='order.type'),
        ),
    ]
