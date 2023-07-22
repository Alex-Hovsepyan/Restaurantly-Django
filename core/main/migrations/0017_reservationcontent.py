# Generated by Django 4.2.3 on 2023-07-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_eventslide'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeholder1', models.CharField(max_length=50, verbose_name='Input Placeholder 1')),
                ('placeholder1_ru', models.CharField(max_length=50, null=True, verbose_name='Input Placeholder 1')),
                ('placeholder1_en', models.CharField(max_length=50, null=True, verbose_name='Input Placeholder 1')),
                ('placeholder2', models.CharField(max_length=50, verbose_name='Input Placeholder 2')),
                ('placeholder2_ru', models.CharField(max_length=50, null=True, verbose_name='Input Placeholder 2')),
                ('placeholder2_en', models.CharField(max_length=50, null=True, verbose_name='Input Placeholder 2')),
                ('placeholder3', models.CharField(max_length=50, verbose_name='Input Placeholder 3')),
                ('placeholder3_ru', models.CharField(max_length=50, null=True, verbose_name='Input Placeholder 3')),
                ('placeholder3_en', models.CharField(max_length=50, null=True, verbose_name='Input Placeholder 3')),
                ('placeholder4', models.CharField(max_length=50, verbose_name='Input Placeholder 4')),
                ('placeholder4_ru', models.CharField(max_length=50, null=True, verbose_name='Input Placeholder 4')),
                ('placeholder4_en', models.CharField(max_length=50, null=True, verbose_name='Input Placeholder 4')),
                ('placeholder5', models.CharField(max_length=50, verbose_name='Input Placeholder 5')),
                ('placeholder5_ru', models.CharField(max_length=50, null=True, verbose_name='Input Placeholder 5')),
                ('placeholder5_en', models.CharField(max_length=50, null=True, verbose_name='Input Placeholder 5')),
                ('btn_name', models.CharField(max_length=40, verbose_name='Button Name')),
                ('btn_name_ru', models.CharField(max_length=40, null=True, verbose_name='Button Name')),
                ('btn_name_en', models.CharField(max_length=40, null=True, verbose_name='Button Name')),
            ],
            options={
                'verbose_name': 'Reservation Content',
                'verbose_name_plural': 'Reservation Content',
            },
        ),
    ]
