# Generated by Django 2.2.11 on 2020-03-27 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='Data Inicio')),
                ('end_date', models.DateTimeField(verbose_name='Data Fim')),
                ('classification', models.IntegerField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True, verbose_name='Nota')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'trip',
            },
        ),
    ]