# Generated by Django 5.0.1 on 2024-01-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TNC', '0011_remove_mesure_like_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesure',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]
