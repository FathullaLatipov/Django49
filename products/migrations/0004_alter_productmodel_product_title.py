# Generated by Django 4.2.11 on 2024-03-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productmodel_product_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_title',
            field=models.CharField(help_text='Тут добавьте названия товара', max_length=50, verbose_name='product_title'),
        ),
    ]