# Generated by Django 4.2.3 on 2023-08-09 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_alter_blog_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/'),
        ),
    ]