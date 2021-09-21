from django.shortcuts import render
from django.http import Http404
from .models import Recipe
from bson.objectid import ObjectId

def recipe_detail_view(request, id):
    try:
        recipe = Recipe.objects.get(_id=ObjectId(id))
    except:
        raise Http404

    context = {
        'recipe': recipe
    }
    
    return render(request, 'recipes/details.html', context)

