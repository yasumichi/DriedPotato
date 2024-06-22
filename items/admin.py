from django.contrib import admin

# Register your models here.

from .models import ItemCategory, Item, Comment

admin.site.register(ItemCategory)
admin.site.register(Item)
admin.site.register(Comment)
