# ⚽ Football Stats API

Это мой первый проект на Django, который я пишу только в учебных целях. Здесь я учусь работать с Django, Django REST Framework и основами построения API. В будущем планирую расширять проект, поэтому список API эндпоинтов вынесен в отдельный файл [`API_ENDPOINTS.md`](./API_ENDPOINTS.md) для удобства поддержки и масштабирования.

## 🚀 Возможности

- 📁 CRUD для футбольных команд (Teams)
- 📁 CRUD для игроков (Players)
- 📁 CRUD для турниров (Tournaments)
- 📁 CRUD для матчей (Matches)
- 📊 Получение статистики по командам, игрокам и матчам

## 🖥️ Технологии

- Python 3.x
- Django
- Django REST Framework
- SQLite (по умолчанию)

## 📦 Установка проекта

```bash
# Клонируем репозиторий
git clone https://github.com/rohnroses/footballstats.git
cd footballstats

# Устанавливаем зависимости
pipenv install
pipenv shell

# Миграции базы данных
python manage.py migrate

# Запускаем сервер
python manage.py runserver
```

## 🔗 API endpoints

> Список всех эндпоинтов теперь находится в отдельном файле [`API_ENDPOINTS.md`](./API_ENDPOINTS.md).

## 🛠️ Будущие улучшения

* 📌 Swagger-документация API
* 📌 Перевести проект на PostgreSQL
* 📌 Docker-контейнеризация
* 📌 Вынести документацию по API в отдельный файл

## 🧾 Лицензия

License © 2025 [rohnroses](https://github.com/rohnroses)