# Generated by Django 4.2.1 on 2023-05-20 03:12

from django.conf import settings
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tourney_time', '0002_alter_tournament_date4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.TextField()),
                ('date', models.DateField()),
                ('partners', django.contrib.postgres.fields.hstore.HStoreField()),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourney_time.tournament')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
