# Generated by Django 5.1.2 on 2024-10-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20190407_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_now',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Текущая цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_old',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Предыдущая цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=models.TextField(blank=True, verbose_name='Характеристики'),
        ),
    ]
