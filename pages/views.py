import recipes
from django.shortcuts import render
from recipes.models import Recipe

ITEMS_PER_PAGE = 6

def index_view(request):
    queryset = Recipe.objects.all()[:ITEMS_PER_PAGE]

    context =  {
        "recipe_list":queryset
    }

    return render(request, 'index.html', context)

def page_view(request, page_num):
    queryset = Recipe.objects.all()[(page_num * ITEMS_PER_PAGE):((page_num + 1)*ITEMS_PER_PAGE)]

    context =  {
        "recipe_list":queryset,
        "page_indexes": [x for x in range(page_num, page_num + 4)]
    }

    return render(request, 'index.html', context)
