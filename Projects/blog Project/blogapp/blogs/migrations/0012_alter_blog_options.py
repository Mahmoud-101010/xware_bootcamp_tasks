# Generated by Django 4.2.3 on 2023-08-10 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_alter_blog_post_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-timestamp']},
        ),
    ]
