# Generated by Django 5.1.4 on 2025-01-07 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_website', '0006_alter_aboutme_social_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutme',
            old_name='about_me',
            new_name='description',
        ),
    ]
