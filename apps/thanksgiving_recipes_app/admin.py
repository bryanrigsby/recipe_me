from django.contrib import admin

from .models import UserImage, RecipeImage

admin.site.register(UserImage)
admin.site.register(RecipeImage)