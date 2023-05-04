# Generated by Django 4.0.4 on 2023-04-19 20:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='participantes',
            field=models.ManyToManyField(null=True, related_name='evento_participante', to=settings.AUTH_USER_MODEL),
        ),
    ]
