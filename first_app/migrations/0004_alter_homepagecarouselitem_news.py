# Generated by Django 4.2.1 on 2023-07-08 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecarouselitem',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='first_app.news', verbose_name='Новость'),
        ),
    ]
