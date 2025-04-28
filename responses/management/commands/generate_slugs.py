from django.core.management.base import BaseCommand
from responses.models import Category

class Command(BaseCommand):
    help = 'Генерирует slug\'ы для всех категорий'

    def handle(self, *args, **options):
        categories = Category.objects.all()
        for category in categories:
            if not category.slug:
                category.save()  # Это вызовет метод save(), который сгенерирует slug
                self.stdout.write(f'Сгенерирован slug для категории "{category.name}": {category.slug}')
            else:
                self.stdout.write(f'Категория "{category.name}" уже имеет slug: {category.slug}') 