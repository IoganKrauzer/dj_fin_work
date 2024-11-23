from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from recipapp.models import Recipe


class RecipesListView(ListView):
    queryset = (
        Recipe.objects
        .select_related('author', 'category')
    )


class RecipesDetailView(DetailView):
    queryset = (
        Recipe.objects
        .select_related('author', 'category')
    )


class RecipesCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ('title',
              'category',
              'description',
              'cooking_steps',
              'cooking_time',
              'author',
              )
    success_url = reverse_lazy('recipapp:index')


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ('title',
              'category',
              'description',
              'cooking_steps',
              'cooking_time',
              )
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('recipapp:index')

    def get_success_url(self):
        return reverse(
            'recipapp:recipe_detail',
            kwargs={'pk': self.object.pk}
        )


class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipapp:recipes-list')


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'base.html')


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipapp/index.html')
