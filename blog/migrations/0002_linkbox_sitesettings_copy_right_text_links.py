# Generated by Django 4.2.4 on 2023-08-25 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='copy_right_text',
            field=models.CharField(default='hello', max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=130)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.linkbox')),
            ],
        ),
    ]
