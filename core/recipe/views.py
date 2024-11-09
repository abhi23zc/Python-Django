from django.shortcuts import render, redirect
from .models import *

def recipes(request):
    if(request.method == "POST"):
        
        data = request.POST
        name =data.get('recipe_name') 
        desc = data.get('recipe_desc')
        img = (request.FILES.get('recipe_image'))
        
        Recipe.objects.create(
            recipe_name = name, 
            recipe_image = img, 
            recipe_desc = desc
        )
        
        return redirect("/recipes/")
    
    querySet = Recipe.objects.all()
    context = {'recipes':querySet}
    return render(request, 'recipes.html', context) 
