# Generated by Django 2.0.2 on 2018-07-23 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='library',
        ),
        migrations.AddField(
            model_name='book',
            name='library',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='catalog.Library', verbose_name='Biblioteca'),
            preserve_default=False,
        ),
    ]
