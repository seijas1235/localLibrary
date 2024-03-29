# Generated by Django 2.0.2 on 2018-07-31 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departmento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depto', models.CharField(max_length=75, verbose_name='Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Escolaridad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Escolaridad')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Municipio')),
                ('depto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Departmento')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='cui',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
