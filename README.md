# Practika

Учебный Python-проект с PostgreSQL и FastAPI.

## Что реализовано

В проект добавлен API для работы с каталогом книг.

Сделано:

- подключение к PostgreSQL;
- SQLAlchemy-модели Category и Book;
- Pydantic-схемы для API;
- CRUD для категорий;
- CRUD для книг;
- фильтрация книг по категории;
- endpoint /health;
- Swagger-документация;
- проверка данных в PostgreSQL.

## Структура проекта

app/
  api/
    category_routes.py
    book_routes.py
  db.py
  models.py
  crud.py
  init_db.py
  main.py
  schemas.py

examples/
  database_result.jpg
  swagger_page.png
  api_books_request.png
  postgres_tables.png

.gitignore
requirements.txt
README.md

## Локальная настройка

Для запуска проекта в корне должен быть файл .env.

Содержимое .env:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345

Файл .env не загружается в GitHub, потому что он добавлен в .gitignore.

## Установка зависимостей

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Подготовка базы

python3 app/init_db.py

## Запуск API

uvicorn app.main:app --reload

После запуска можно открыть:

http://127.0.0.1:8000/docs

## Проверка

Основные адреса:

GET /health

GET /categories/

POST /categories/

GET /books/

GET /books/?category_id=1

POST /books/
