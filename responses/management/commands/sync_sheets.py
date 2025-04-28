from django.core.management.base import BaseCommand
from responses.google_sheets import sync_with_google_sheets

class Command(BaseCommand):
    help = 'Синхронизирует данные с Google Sheets'

    def handle(self, *args, **options):
        try:
            sync_with_google_sheets()
            self.stdout.write(self.style.SUCCESS('Синхронизация успешно завершена'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при синхронизации: {str(e)}')) 