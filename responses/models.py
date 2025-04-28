from django.db import models
from django.utils.text import slugify
from django.db.models import Max

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родительская категория')
    slug = models.SlugField(unique=True, blank=True)
    order = models.IntegerField(default=0, verbose_name='Порядок')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            # Генерируем базовый slug из имени, транслитерируя кириллицу
            base_slug = slugify(self.name, allow_unicode=False)
            if not base_slug:  # Если имя состоит только из не-ASCII символов
                base_slug = 'category'
            
            slug = base_slug
            counter = 1
            
            # Проверяем существование slug'а и добавляем число, если нужно
            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
                
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Response(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='responses', verbose_name='Категория')
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')
    tags = models.CharField(max_length=255, blank=True, verbose_name='Теги')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.question[:50]}..."
