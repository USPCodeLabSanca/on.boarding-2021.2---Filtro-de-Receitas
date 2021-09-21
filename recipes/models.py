from django.db.models.fields import TextField
from djongo import models

class Recipe(models.Model):
    _id = models.ObjectIdField()
    author = models.TextField()
    cook_time_minutes = models.IntegerField()
    description = models.TextField()
    error = models.BooleanField()
    footnotes = models.JSONField()
    ingredients = models.JSONField()
    instructions = models.JSONField()
    photo_url = models.URLField()
    prep_time_minutes = models.IntegerField()
    rating_stars = models.FloatField()
    review_count = models.IntegerField()
    time_scraped = models.IntegerField()
    title = models.TextField()
    total_time_minutes = models.IntegerField()
    url = models.URLField()
    keywords = models.JSONField()


