# Generated by Django 3.2.7 on 2021-09-21 16:35

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('author', models.TextField()),
                ('cook_time_minutes', models.IntegerField()),
                ('description', models.TextField()),
                ('error', models.BooleanField()),
                ('footnotes', djongo.models.fields.JSONField()),
                ('ingredients', djongo.models.fields.JSONField()),
                ('instructions', djongo.models.fields.JSONField()),
                ('photo_url', models.URLField()),
                ('prep_time_minutes', models.IntegerField()),
                ('rating_stars', models.FloatField()),
                ('review_count', models.IntegerField()),
                ('time_scraped', models.IntegerField()),
                ('title', models.TextField()),
                ('total_time_minutes', models.IntegerField()),
                ('url', models.URLField()),
                ('keywords', djongo.models.fields.JSONField()),
            ],
        ),
    ]
