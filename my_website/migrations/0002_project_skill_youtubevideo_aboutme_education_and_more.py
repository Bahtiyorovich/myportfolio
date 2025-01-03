# Generated by Django 5.1.4 on 2024-12-23 09:17

import django.db.models.deletion
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter your project title', max_length=100, unique=True)),
                ('slug', models.SlugField(help_text='Enter your project slug', unique=True)),
                ('description', tinymce.models.HTMLField(help_text='Enter description')),
                ('create_date', models.CharField(help_text='Enter start date', max_length=4)),
                ('service', models.CharField(help_text='Enter service', max_length=100)),
                ('client', models.CharField(help_text='Enter client', max_length=100)),
                ('project_type', models.CharField(help_text='Enter project type', max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your skill name', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter your video title', max_length=100)),
                ('link', models.URLField(help_text='Enter Youtube video link')),
                ('thumbnail', models.ImageField(help_text='Enter Youtube video thumbnail', upload_to='image/youtube_thumbnail')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', tinymce.models.HTMLField(blank=True, help_text='Write something about me', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_me/image')),
                ('my_name', models.CharField(help_text='Enter your name', max_length=30)),
                ('social_media', models.JSONField(blank=True, help_text='Add your social media links', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(blank=True, help_text='Add your skills', to='my_website.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(help_text='Enter start year', max_length=4)),
                ('end_year', models.CharField(help_text='Enter end year', max_length=4)),
                ('degree', models.CharField(help_text='Enter degree', max_length=100)),
                ('university', models.CharField(help_text='Enter university', max_length=100)),
                ('description', tinymce.models.HTMLField(help_text='Enter description')),
                ('about_me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_website.aboutme')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(help_text='Enter start year', max_length=4)),
                ('end_year', models.CharField(help_text='Enter end year', max_length=4)),
                ('position', models.CharField(help_text='Enter position', max_length=100)),
                ('company', models.CharField(help_text='Enter company', max_length=100)),
                ('description', tinymce.models.HTMLField(help_text='Enter description')),
                ('about_me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_website.aboutme')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='project/image')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_website.project')),
            ],
        ),
    ]
