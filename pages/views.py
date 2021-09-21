from django.shortcuts import render
from recipes.models import Recipe

def index_view(request):
    return render(request, 'index.html', {})

def recipe_view(request):
    recipe = Recipe.objects.all()[:1][0]
    
    context = {
        "_id" : recipe._id,
        "author" : recipe.author,
        "cook_time_minutes" : recipe.cook_time_minutes,
        "description" : recipe.description,
        "error" : recipe.error,
        "footnotes" : recipe.footnotes,
        "ingredients" : recipe.ingredients,
        "instructions" : recipe.instructions,
        "photo_url" : recipe.photo_url,
        "prep_time_minutes" : recipe.prep_time_minutes,
        "rating_stars" : recipe.rating_stars,
        "review_count" : recipe.review_count,
        "time_scraped" : recipe.time_scraped,
        "title": recipe.title,
        "total_time_minutes" : recipe.total_time_minutes,
        "url": recipe.url,
        "keywords": recipe.keywords,
    }
    
    return render(request, 'recipe.html', context)
