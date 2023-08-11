# Generated by Django 4.2.3 on 2023-08-09 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_blog_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='imgages/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
