import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from responses.models import Category, Response

print("Проверка содержимого базы данных:")
print(f"Количество категорий: {Category.objects.count()}")
print(f"Количество ответов: {Response.objects.count()}")

print("\nСписок категорий:")
for category in Category.objects.all():
    print(f"- {category.name} (ID: {category.id})")
    
print("\nСписок ответов:")
for response in Response.objects.all():
    print(f"- {response.question} (ID: {response.id})") 