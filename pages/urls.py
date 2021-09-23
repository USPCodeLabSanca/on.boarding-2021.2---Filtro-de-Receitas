from django.contrib import admin
from django.urls import path

from .views import index_view, page_view, rating_page_view, search_page_view, search_with_filter_page_view, time_page_view
from recipes.views import recipe_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('pages/<int:page_num>', page_view, name='page'),
    path('recipe/<str:id>/', recipe_detail_view, name='recipe'),
    path('search/<str:ingredients>&&<int:page_num>/', search_page_view, name='search'),
    path('filter/time/<int:limit_time>&&<int:page_num>/', time_page_view, name='time_filter'),
    path('popular/<int:page_num>/', rating_page_view, name='rating_filter'),
    path('search/filter/<int:limit_time>&&<str:ingredients>&&<int:page_num>/', search_with_filter_page_view, name='search_with_filter'),
]
