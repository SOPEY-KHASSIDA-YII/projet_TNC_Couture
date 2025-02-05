# Generated by Django 5.0.1 on 2024-10-07 20:06

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mesure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('tel', models.IntegerField()),
                ('genre', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme')], max_length=5)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)])),
                ('page_officielle', models.URLField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('epaule', models.IntegerField()),
                ('longueur_bb', models.IntegerField()),
                ('coup', models.IntegerField()),
                ('bras', models.IntegerField()),
                ('longueur_pt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('mesure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TNC.mesure')),
            ],
        ),
    ]
