# Generated by Django 4.2 on 2024-07-18 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blogs/')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('description', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='celulares/')),
                ('stock', models.IntegerField(default=0)),
                ('marca', models.ManyToManyField(to='TecnoMovilApp.categoria')),
            ],
            options={
                'verbose_name_plural': 'Celulares',
            },
        ),
    ]