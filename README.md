# Practika

Учебный Python-проект с подключением к PostgreSQL.

## Что реализовано

В проект добавлена работа с базой данных через SQLAlchemy.

Сделано:

- подключение к PostgreSQL;
- модели Category и Book;
- создание таблиц;
- CRUD-операции для категорий и книг;
- заполнение базы стартовыми данными;
- вывод данных из базы в терминал.

## Структура проекта

app/
  db.py
  models.py
  crud.py
  init_db.py
  main.py

examples/
  database_result.png

.gitignore
requirements.txt
README.md

## Локальные настройки

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

## Запуск

python3 app/main.py
