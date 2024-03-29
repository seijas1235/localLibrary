# Generated by Django 2.0.2 on 2018-07-24 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20180724_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='tokem',
            field=models.CharField(default='MCrL5MAgMPHyBUpU', max_length=16, verbose_name='Token'),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Countries', verbose_name='Pais'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Author', verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Genre', verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='book',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Library', verbose_name='Biblioteca'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Book', verbose_name='Libro'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.State', verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
