from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Response

# Create your views here.

def category_list(request):
    root_categories = Category.objects.filter(parent=None).order_by('name')
    
    # Добавляем поиск по тегам
    tag_query = request.GET.get('tag', '')
    responses = Response.objects.all()
    
    if tag_query:
        responses = responses.filter(tags__icontains=tag_query)
    
    return render(request, 'responses/category_list.html', {
        'root_categories': root_categories,
        'responses': responses,
        'tag_query': tag_query,
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    responses = Response.objects.all()  # Берем все ответы, а не только из категории
    
    # Добавляем поиск по тегам
    tag_query = request.GET.get('tag', '')
    if tag_query:
        responses = responses.filter(tags__icontains=tag_query)
    else:
        # Если поиск не активен, показываем только ответы из текущей категории
        responses = responses.filter(category=category)
    
    root_categories = Category.objects.filter(parent=None).order_by('name')
    
    return render(request, 'responses/category_list.html', {
        'category': category,
        'current_category': category,
        'responses': responses,
        'root_categories': root_categories,
        'tag_query': tag_query,
    })
