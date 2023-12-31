# Generated by Django 4.2.3 on 2023-07-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header_Sidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_title', models.CharField(max_length=50, verbose_name='Document Title')),
                ('doc_title_ru', models.CharField(max_length=50, null=True, verbose_name='Document Title')),
                ('doc_title_en', models.CharField(max_length=50, null=True, verbose_name='Document Title')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('phone_number_ru', models.CharField(max_length=20, null=True, verbose_name='Phone Number')),
                ('phone_number_en', models.CharField(max_length=20, null=True, verbose_name='Phone Number')),
                ('open_times', models.CharField(max_length=50, verbose_name='Open Times')),
                ('open_times_ru', models.CharField(max_length=50, null=True, verbose_name='Open Times')),
                ('open_times_en', models.CharField(max_length=50, null=True, verbose_name='Open Times')),
                ('language1', models.CharField(max_length=5, verbose_name='Language 1')),
                ('language1_ru', models.CharField(max_length=5, null=True, verbose_name='Language 1')),
                ('language1_en', models.CharField(max_length=5, null=True, verbose_name='Language 1')),
                ('language2', models.CharField(max_length=5, verbose_name='Language 2')),
                ('language2_ru', models.CharField(max_length=5, null=True, verbose_name='Language 2')),
                ('language2_en', models.CharField(max_length=5, null=True, verbose_name='Language 2')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('path1', models.CharField(max_length=50, verbose_name='Path 1')),
                ('path1_ru', models.CharField(max_length=50, null=True, verbose_name='Path 1')),
                ('path1_en', models.CharField(max_length=50, null=True, verbose_name='Path 1')),
                ('path2', models.CharField(max_length=50, verbose_name='Path 2')),
                ('path2_ru', models.CharField(max_length=50, null=True, verbose_name='Path 2')),
                ('path2_en', models.CharField(max_length=50, null=True, verbose_name='Path 2')),
                ('path3', models.CharField(max_length=50, verbose_name='Path 3')),
                ('path3_ru', models.CharField(max_length=50, null=True, verbose_name='Path 3')),
                ('path3_en', models.CharField(max_length=50, null=True, verbose_name='Path 3')),
                ('path4', models.CharField(max_length=50, verbose_name='Path 4')),
                ('path4_ru', models.CharField(max_length=50, null=True, verbose_name='Path 4')),
                ('path4_en', models.CharField(max_length=50, null=True, verbose_name='Path 4')),
                ('path5', models.CharField(max_length=50, verbose_name='Path 5')),
                ('path5_ru', models.CharField(max_length=50, null=True, verbose_name='Path 5')),
                ('path5_en', models.CharField(max_length=50, null=True, verbose_name='Path 5')),
                ('path6', models.CharField(max_length=50, verbose_name='Path 6')),
                ('path6_ru', models.CharField(max_length=50, null=True, verbose_name='Path 6')),
                ('path6_en', models.CharField(max_length=50, null=True, verbose_name='Path 6')),
                ('path7', models.CharField(max_length=50, verbose_name='Path 7')),
                ('path7_ru', models.CharField(max_length=50, null=True, verbose_name='Path 7')),
                ('path7_en', models.CharField(max_length=50, null=True, verbose_name='Path 7')),
                ('path8', models.CharField(max_length=50, verbose_name='Path 8')),
                ('path8_ru', models.CharField(max_length=50, null=True, verbose_name='Path 8')),
                ('path8_en', models.CharField(max_length=50, null=True, verbose_name='Path 8')),
                ('btn_name', models.CharField(max_length=50, verbose_name='Button Name')),
                ('btn_name_ru', models.CharField(max_length=50, null=True, verbose_name='Button Name')),
                ('btn_name_en', models.CharField(max_length=50, null=True, verbose_name='Button Name')),
            ],
            options={
                'verbose_name': 'Header_Sidebar',
                'verbose_name_plural': 'Header_Sidebar',
            },
        ),
    ]
