# Generated by Django 4.2.8 on 2024-11-03 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_index', '0003_alter_personaldetails_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personaldetails',
            old_name='github url',
            new_name='github_url',
        ),
        migrations.RenameField(
            model_name='personaldetails',
            old_name='Linkedin url',
            new_name='linkedin_url',
        ),
    ]