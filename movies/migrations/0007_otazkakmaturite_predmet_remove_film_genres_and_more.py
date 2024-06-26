# Generated by Django 4.0.3 on 2024-05-12 20:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_delete_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='otazkakmaturite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('plot', models.TextField(blank=True, null=True, verbose_name='Plot')),
                ('release_date', models.DateField(blank=True, help_text='Please use the following format: <em>YYYYMM-DD</em>.', null=True, verbose_name='Release date')),
                ('runtime', models.IntegerField(blank=True, help_text='Please enter an integer value (minutes)', null=True, verbose_name='Runtime')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='film/posters/%Y/%m/%d/', verbose_name='Poster')),
                ('rate', models.FloatField(default=5.0, help_text='Please enter an float value (range 1.0 - 10.0)', null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='Rate')),
            ],
            options={
                'verbose_name': 'otazkakmaturite',
                'verbose_name_plural': 'otazkakmaturite',
                'ordering': ['-release_date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='predmet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Přidej k maturitní otázce předmět (PVY, PRP)', max_length=50, unique=True, verbose_name='Nazev předmětu')),
            ],
            options={
                'verbose_name': 'předmět',
                'verbose_name_plural': 'předmět',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='film',
            name='genres',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='otazkakmaturite',
            name='genres',
            field=models.ManyToManyField(help_text='Zvol předmět pro tuto maturitní otázku', to='movies.predmet'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.otazkakmaturite'),
        ),
        migrations.DeleteModel(
            name='Film',
        ),
    ]
