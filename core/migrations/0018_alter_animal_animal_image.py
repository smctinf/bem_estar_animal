# Generated by Django 3.2.13 on 2023-02-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_animal_animal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animal_image',
            field=models.ImageField(blank=True, null=True, upload_to='animais/'),
        ),
    ]