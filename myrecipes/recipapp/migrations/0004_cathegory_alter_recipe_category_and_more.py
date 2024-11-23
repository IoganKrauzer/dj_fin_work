# Generated by Django 5.1.3 on 2024-11-23 03:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipapp', '0003_alter_cathegoryrecipe_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cathegory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipapp.cathegory', verbose_name='Категория'),
        ),
        migrations.DeleteModel(
            name='CathegoryRecipe',
        ),
    ]
