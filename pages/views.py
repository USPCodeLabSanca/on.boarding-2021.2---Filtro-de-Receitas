from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
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

# dont ready yet
def search_page_view(request, page_num, ingredients):
    ingredients_list = ingredients.split()
    queryset = []

    # not sure about this, my friends !!!
    queryset += Recipe.objects.filter(reduce(or_, [Q(keywords__contains=x) for x in ingredients_list]))

    queryset = queryset[(page_num * ITEMS_PER_PAGE):((page_num + 1)*ITEMS_PER_PAGE)]

    context =  {
        "recipe_list":queryset,
        "page_indexes": [x for x in range(page_num - 1 if page_num > 0 else page_num, page_num + 4)]
    }

    return render(request, 'index.html', context)