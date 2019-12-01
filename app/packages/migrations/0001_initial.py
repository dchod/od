# Generated by Django 2.2.7 on 2019-12-01 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(max_length=255, verbose_name='Nazwa')),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField(verbose_name='URL')),
                ('author_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Autor')),
                ('author_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email autora')),
                ('current_version', models.CharField(blank=True, max_length=10, null=True, verbose_name='Aktualna wersja')),
                ('description', models.TextField(verbose_name='Opis')),
            ],
            options={
                'verbose_name': 'Pakiet',
                'verbose_name_plural': 'Pakiety',
                'unique_together': {('guid',)},
            },
        ),
        migrations.CreateModel(
            name='Maintainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='zarządca')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.Package', verbose_name='Pakiet')),
            ],
            options={
                'verbose_name': 'zarządca',
                'verbose_name_plural': 'zarządcy',
                'unique_together': {('package', 'name')},
            },
        ),
    ]
