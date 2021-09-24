from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.http import request
import recipes
from django.shortcuts import render
from recipes.models import Recipe
from operator import and_, or_
from functools import reduce

ITEMS_PER_PAGE = 6

def index_view(request):
    queryset = Recipe.objects.all()[:ITEMS_PER_PAGE]

    context =  {
        "recipe_list":queryset,
        "page_indexes": [x for x in range(0, 4)]
    }

    return render(request, 'index.html', context)

def page_view(request, page_num):
    queryset = Recipe.objects.all()[(page_num * ITEMS_PER_PAGE):((page_num + 1)*ITEMS_PER_PAGE)]

    context =  {
        "recipe_list":queryset,
        "page_indexes": [x for x in range(page_num - 1 if page_num > 0 else page_num, page_num + 4)]
    }

    return render(request, 'index.html', context)

def search_page_view(request, page_num, ingredients):
    ingredients = ingredients.strip()
    if len(ingredients) == 0:
        return page_view(request, page_num)

    ingredients_list = ingredients.split('+')

    queryset = Recipe.objects.filter(reduce(and_, [Q(keywords__contains=x) for x in ingredients_list]))\
             .order_by('-rating_stars')

    queryset = queryset[(page_num * ITEMS_PER_PAGE):((page_num + 1)*ITEMS_PER_PAGE)]

    context =  {
        "recipe_list":queryset,
        "page_indexes": [x for x in range(page_num - 1 if page_num > 0 else page_num, page_num + 4)]
    }

    return render(request, 'index.html', context)

def time_page_view(request, page_num, limit_time):
    if limit_time == 0:
        return page_view(request, page_num)
        
    queryset = Recipe.objects.filter(total_time_minutes__lte=limit_time)\
                .order_by('-rating_stars')\
                [(page_num * ITEMS_PER_PAGE):((page_num + 1)*ITEMS_PER_PAGE)]

    context =  {
        "recipe_list": queryset,
        "page_indexes": [x for x in range(page_num - 1 if page_num > 0 else page_num, page_num + 4)]
    }
    return render(request, 'index.html', context)

def rating_page_view(request, page_num):
    queryset = Recipe.objects.order_by('-rating_stars')\
                [(page_num * ITEMS_PER_PAGE):((page_num + 1)*ITEMS_PER_PAGE)]

    context =  {
        "recipe_list": queryset,
        "page_indexes": [x for x in range(page_num - 1 if page_num > 0 else page_num, page_num + 4)]
    }
    return render(request, 'index.html', context)

def search_with_filter_page_view(request, page_num, ingredients, limit_time):
    ingredients = ingredients.strip()

    if len(ingredients) == 0:
        return time_page_view(request, page_num, limit_time)
    
    if limit_time == 0:
        return search_page_view(request, page_num, ingredients)
    
    ingredients_list = ingredients.split()

    queryset = Recipe.objects.filter(total_time_minutes__lte=limit_time)\
                .filter(reduce(or_, [Q(keywords__contains=x) for x in ingredients_list]))\
                .order_by('-rating_stars')

    queryset = queryset[(page_num * ITEMS_PER_PAGE):((page_num + 1)*ITEMS_PER_PAGE)]

    context =  {
        "recipe_list":queryset,
        "page_indexes": [x for x in range(page_num - 1 if page_num > 0 else page_num, page_num + 4)]
    }

    return render(request, 'index.html', context)