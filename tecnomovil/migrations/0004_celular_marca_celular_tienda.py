# Generated by Django 4.2 on 2024-07-17 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnomovil', '0003_alter_celular_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='celular',
            name='marca',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celular',
            name='tienda',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]