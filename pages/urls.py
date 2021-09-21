from django.contrib import admin
from django.urls import path

from .views import index_view, recipe_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('recipe/', recipe_view, name='recipe'),
]
