from django.urls import path

from .views import index, RecipesCreateView, RecipeUpdateView, RecipesListView, RecipesDetailView, RecipeDeleteView

app_name = 'recipapp'

urlpatterns = [
    path('index/', index, name='index'),
    path('list/', RecipesListView.as_view(), name='recipes-list'),
    path('list/create/', RecipesCreateView.as_view(), name='create_recipe'),
    path('list/<int:pk>/', RecipesDetailView.as_view(), name='recipe_detail'),
    path('list/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe_update'),
    path('list/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),

]
