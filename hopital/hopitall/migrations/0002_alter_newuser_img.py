# Generated by Django 4.0.5 on 2022-06-06 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopitall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
