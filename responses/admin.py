from django.contrib import admin
from .models import Category, Response

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'order')
    list_filter = ('parent',)
    search_fields = ('name',)
    ordering = ('order', 'name')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('question', 'answer', 'tags')
    ordering = ('-updated_at',)
