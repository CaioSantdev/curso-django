from django.shortcuts import render,get_list_or_404
from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.all().filter(is_published=True)
    return render(request,'recipes/pages/home.html',context={'recipes':recipes,})

def category(request,category_id):
    # recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    
    recipes = get_list_or_404(Recipe,category__id=category_id,is_published=True)
    return render(request,'recipes/pages/home.html',context={'recipes':recipes,
                                                             'title':f'{recipes[0].category.name} - Category | '})

def recipe(request,id):
    return render(request,'recipes/pages/recipe-view.html',context={
        'recipe':make_recipe(),
        'is_detail_page':True                                                    
    })



