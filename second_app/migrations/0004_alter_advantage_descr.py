# Generated by Django 4.2.1 on 2023-06-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0003_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advantage',
            name='descr',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Описание'),
        ),
    ]
