# ⚽ Football Stats API

Простое API на Django REST Framework для управления футбольными командами, игроками, турнирами и матчами.

## 🚀 Возможности

- 📁 CRUD для футбольных команд (Teams)
- 📁 Расширяемая структура → добавим Игроков, Турниры, Матчи

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

🔗 API endpoints
Метод	Endpoint	Назначение
GET	/api/teams/	Получить список команд
POST	/api/teams/	Добавить новую команду
GET	/api/teams/<id>/	Получить команду по ID
PUT	/api/teams/<id>/	Обновить команду
DELETE	/api/teams/<id>/	Удалить команду

🛠️ Будущие улучшения

    📌 Добавить игроков, турниры, матчи

    📌 Swagger-документация API

    📌 Перевести проект на PostgreSQL

    📌 Docker-контейнеризация

🧾 Лицензия

MIT License © 2025 rohnroses    