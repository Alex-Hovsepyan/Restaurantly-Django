# Generated by Django 4.2.3 on 2023-07-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_menucontent_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucontent',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
    ]
