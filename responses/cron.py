from django_crontab.crontab import Crontab
from .google_sheets import sync_with_google_sheets

def sync_data():
    try:
        sync_with_google_sheets()
        return True
    except Exception as e:
        print(f"Ошибка при синхронизации: {str(e)}")
        return False

# Регистрируем задачу для выполнения каждые 30 минут
CRONJOBS = [
    ('*/30 * * * *', 'responses.cron.sync_data')
] 