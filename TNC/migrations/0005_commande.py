# Generated by Django 5.0.1 on 2024-01-27 11:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TNC', '0004_delete_commande'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('tel', models.IntegerField(verbose_name=10)),
                ('genre', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme')], max_length=5)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)])),
            ],
        ),
    ]
