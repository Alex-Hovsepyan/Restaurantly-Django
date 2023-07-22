# Generated by Django 4.2.3 on 2023-07-21 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_homepage_colored_title_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(upload_to='', verbose_name='Background')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('text1', models.TextField(verbose_name='Text 1')),
                ('text2', models.TextField(verbose_name='Text 2')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50, verbose_name='Icon')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'About Content',
                'verbose_name_plural': 'About Content',
            },
        ),
    ]