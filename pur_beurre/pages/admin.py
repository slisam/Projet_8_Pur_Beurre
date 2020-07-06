from django.contrib import admin

# Register your models here.
from .models import Category, Food, MySelection

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(MySelection)
