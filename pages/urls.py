from django.contrib import admin
from django.urls import path

from .views import index_view, page_view, search_page_view
from recipes.views import recipe_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('pages/<int:page_num>', page_view, name='page'),
    path('recipe/<str:id>/', recipe_detail_view, name='recipe'),

    # dont know if it's correct
    path('search/<int:page_num>&&<str:ingredients>/', search_page_view, name='search'),

]
