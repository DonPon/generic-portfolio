# Generated by Django 4.2.8 on 2024-11-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_index', '0002_personaldetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personaldetails',
            options={'verbose_name': 'Personal Details', 'verbose_name_plural': 'Personal Details'},
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='Linkedin url',
            field=models.URLField(blank=True, verbose_name='Linkedin url'),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='github url',
            field=models.URLField(blank=True, verbose_name='github url'),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='details',
            field=models.TextField(blank=True, verbose_name='Extensive details'),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
