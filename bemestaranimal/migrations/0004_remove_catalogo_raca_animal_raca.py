# Generated by Django 4.1.6 on 2023-02-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bemestaranimal', '0003_alter_animal_sexo_alter_catalogo_animal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogo',
            name='raca',
        ),
        migrations.AddField(
            model_name='animal',
            name='raca',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Raça'),
        ),
    ]
