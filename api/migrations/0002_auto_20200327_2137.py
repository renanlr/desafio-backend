# Generated by Django 2.2.11 on 2020-03-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trip',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='trip',
            name='classification',
            field=models.IntegerField(blank=True, choices=[(0, 'Trabalho'), (1, 'Atividade física'), (2, 'Lazer'), (3, 'Deslocamento')], null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Fim'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Inicio'),
        ),
    ]