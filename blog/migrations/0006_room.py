# Generated by Django 4.2.4 on 2023-08-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/room_images')),
                ('price', models.IntegerField()),
                ('bed_count', models.IntegerField()),
                ('bathroom_count', models.IntegerField()),
                ('is_internet', models.BooleanField(default=False)),
                ('is_library', models.BooleanField(default=False)),
            ],
        ),
    ]
