from django.shortcuts import render, redirect
from .models import *

def recipes(request):
    if request.method == "POST":
        name = request.POST.get('recipe_name')
        desc = request.POST.get('recipe_desc')
        img = request.FILES.get('recipe_image')
        
        if name:  # Check if name is not empty
            Recipe.objects.create(
                recipe_name=name, 
                recipe_image=img, 
                recipe_desc=desc
            )
        
        return redirect("/recipes/")
    
    querySet = Recipe.objects.all()
    
    if request.GET.get('search'):
        querySet = querySet.filter(recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': querySet}
    return render(request, 'recipes.html', context) 

def update_recipe(request, id):
    querySet = Recipe.objects.get(id=id)
    context = {'recipe':querySet}
    
    if(request.method == 'POST'):
       
        data = request.POST
        querySet.recipe_desc = data.get('recipe_desc')
        querySet.recipe_name = data.get('recipe_name')
        if(request.FILES):
            
            querySet.recipe_image = request.FILES.get('recipe_image')
        
        querySet.save()
        return redirect("/recipes")
            
    return render(request, 'update_recipe.html', context)

def delete_recipe(request, id):
    
    try:
            
        querySet = Recipe.objects.get(id=id)
        querySet.delete()
    except Exception as e:
        print(e)
    return redirect('/recipes') 


def login(request):
    return render(request, 'login.html')



def signup(request):
    return render(request, 'register.html')