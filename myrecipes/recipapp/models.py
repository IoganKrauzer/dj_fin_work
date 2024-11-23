from django.contrib.auth.models import User
from django.db import models


class Cathegory(models.Model):

    name = models.CharField(max_length=100, blank=False, verbose_name='Название категории')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=150, blank=False, verbose_name="Заголовок рецепта")
    category = models.ForeignKey(Cathegory, on_delete=models.CASCADE, blank=False, verbose_name="Категория")
    description = models.TextField(blank=False, verbose_name="Описание рецепта")
    cooking_steps = models.TextField(blank=False, verbose_name="Шаги приготовления")
    cooking_time = models.DurationField(blank=False, verbose_name="Время приготовления (чч:мм:сс)")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, verbose_name="Автор рецепта")
    created_date = models.DateTimeField(auto_now_add=True)
