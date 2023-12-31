# Generated by Django 4.2.3 on 2023-07-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_special'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('price', models.FloatField(verbose_name='Price')),
                ('text1', models.TextField(verbose_name='Text 1')),
                ('offer1', models.CharField(max_length=80, verbose_name='Offer 1')),
                ('offer2', models.CharField(max_length=80, verbose_name='Offer 2')),
                ('offer3', models.CharField(max_length=80, verbose_name='Offer 3')),
                ('text2', models.TextField(verbose_name='Text 2')),
            ],
            options={
                'verbose_name': 'Event Slide',
                'verbose_name_plural': 'Event Slides',
            },
        ),
    ]
