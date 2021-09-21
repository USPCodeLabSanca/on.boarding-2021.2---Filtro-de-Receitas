from django.contrib import admin
from django.urls import path

from .views import index_view, page_view
from recipes.views import recipe_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('pages/<int:page_num>', page_view, name='page'),
    path('recipe/<str:id>/', recipe_detail_view, name='recipe'),
]
