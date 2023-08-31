# Generated by Django 4.2.4 on 2023-08-30 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_gallerycategory_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='images/blog_images')),
                ('is_publish', models.BooleanField(default=False)),
            ],
        ),
    ]