from django.contrib import admin
from django.urls import path
from home.views import *
from recipe.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('success/', success, name="success"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('admin/', admin.site.urls),
    path('recipes/', recipes, name="recipes"),
    path('delete-recipes/<id>/', delete_recipe, name="recipes"),
    path('update-recipe/<id>/', update_recipe, name="recipes"),

    path('login/', login, name="login"),
    path('signup/', signup, name="signup")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
    

urlpatterns+= staticfiles_urlpatterns()