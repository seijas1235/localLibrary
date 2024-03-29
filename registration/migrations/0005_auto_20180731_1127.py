# Generated by Django 2.0.2 on 2018-07-31 17:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20180731_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='colegio',
            field=models.CharField(max_length=250, null=True, verbose_name='Institucion Educativa'),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de nacimiento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='departmento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.Departmento', verbose_name='Departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='escolaridad',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='registration.Escolaridad', verbose_name='Escolaridad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='genre',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='registration.Genero', verbose_name='Genero'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='municipio',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='registration.Municipio', verbose_name='Municipio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='zona',
            field=models.IntegerField(default=9, verbose_name='Zona'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='cui',
            field=models.CharField(max_length=13, verbose_name='DPI'),
        ),
    ]
