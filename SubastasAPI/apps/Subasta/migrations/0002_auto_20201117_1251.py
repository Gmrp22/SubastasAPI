# Generated by Django 3.1.3 on 2020-11-17 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subasta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subasta',
            name='Estado',
            field=models.CharField(blank=True, default='Espera', max_length=200),
        ),
    ]
