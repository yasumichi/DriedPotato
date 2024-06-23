# Generated by Django 5.0.6 on 2024-06-23 12:50

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_item_approval'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Registered User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='approval',
            field=models.BooleanField(default=False, verbose_name='approval'),
        ),
        migrations.AlterField(
            model_name='item',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Registered User'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='items.itemcategory', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='item code'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=100, verbose_name='item name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='necessity',
            field=models.TextField(verbose_name='necessity'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=19, validators=[django.core.validators.MinValueValidator(1)], verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='priority'),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='quantity'),
        ),
    ]
