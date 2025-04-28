import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings
from .models import Category, Response
from django.utils.text import slugify

def get_google_sheets_client():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        settings.GOOGLE_SHEETS_CREDENTIALS, scope)
    return gspread.authorize(credentials)

def sync_with_google_sheets():
    print("Начинаем синхронизацию...")
    print(f"Используем файл учетных данных: {settings.GOOGLE_SHEETS_CREDENTIALS}")
    print(f"ID таблицы: {settings.GOOGLE_SHEETS_ID}")
    
    try:
        client = get_google_sheets_client()
        print("Успешно подключились к Google Sheets API")
        
        sheet = client.open_by_key(settings.GOOGLE_SHEETS_ID).sheet1
        print("Успешно открыли таблицу")
        
        # Получаем все данные из таблицы
        data = sheet.get_all_records()
        print(f"Получено {len(data)} записей из таблицы")
        
        # Создаем категории и ответы
        categories = {}
        for row in data:
            print(f"Обработка строки: {row}")
            
            # Создаем основную категорию, если её нет
            category_name = row['Категория'].strip()
            if category_name and category_name not in categories:
                category, created = Category.objects.get_or_create(
                    name=category_name,
                    defaults={'slug': slugify(category_name)}
                )
                categories[category_name] = category
                print(f"{'Создана' if created else 'Найдена'} категория: {category_name}")
            
            # Создаем подкатегорию, если она указана
            subcategory = None
            if row['Подкатегория']:
                subcategory_name = row['Подкатегория'].strip()
                full_name = f"{category_name} - {subcategory_name}"
                
                if full_name not in categories:
                    subcategory, created = Category.objects.get_or_create(
                        name=subcategory_name,
                        parent=categories[category_name],
                        defaults={'slug': slugify(subcategory_name)}
                    )
                    categories[full_name] = subcategory
                    print(f"{'Создана' if created else 'Найдена'} подкатегория: {subcategory_name}")
                else:
                    subcategory = categories[full_name]
            
            # Создаем или обновляем ответ
            target_category = subcategory if subcategory else categories[category_name]
            Response.objects.update_or_create(
                question=row['Вопрос'].strip(),
                category=target_category,
                defaults={
                    'answer': row['Ответ'].strip(),
                    'tags': row.get('Тэги', '').strip()
                }
            )
            print(f"Обновлен ответ: {row['Вопрос']}")
        
        print("Синхронизация успешно завершена")
    except Exception as e:
        print(f"Ошибка при синхронизации: {str(e)}")
        raise 