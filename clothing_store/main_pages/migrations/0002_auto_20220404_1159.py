# Generated by Django 3.2.12 on 2022-04-04 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'Под-категории'},
        ),
    ]
