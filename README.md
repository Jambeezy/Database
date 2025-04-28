# Database

Проект для управления рабочими процессами.

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Jambeezy/Database.git
cd Database
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Запустите сервер разработки:
```bash
python manage.py runserver

```

## Структура проекта

- `manage.py` - скрипт управления Django
- `requirements.txt` - зависимости проекта
- `static/` - статические файлы
- `templates/` - шаблоны
- `apps/` - приложения Django

## Лицензия

MIT
