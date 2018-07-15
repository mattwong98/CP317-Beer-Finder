# Generated by Django 2.0.5 on 2018-06-01 17:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beerName', models.CharField(max_length=50)),
                ('colourValue', models.FloatField(default=0.0)),
                ('alcoholVolume', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='BodyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodyTypeName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandName', models.CharField(max_length=50)),
                ('countryOfOrigin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ContainerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('containerTypeName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratingValue', models.IntegerField(default=0)),
                ('raterName', models.CharField(max_length=50)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('beer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Beer')),
            ],
        ),
        migrations.CreateModel(
            name='Taste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasteName', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='beer',
            name='bodyType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.BodyType'),
        ),
        migrations.AddField(
            model_name='beer',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Brand'),
        ),
        migrations.AddField(
            model_name='beer',
            name='containerType',
            field=models.ManyToManyField(blank=True, to='home.ContainerType'),
        ),
        migrations.AddField(
            model_name='beer',
            name='taste',
            field=models.ManyToManyField(blank=True, to='home.Taste'),
        ),
    ]