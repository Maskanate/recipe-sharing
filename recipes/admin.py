from django.contrib import admin
from .models import Profile, Category, Tag, Recipe, Comment, Rating

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Rating)