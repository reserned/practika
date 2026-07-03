import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from app.crud import (
    clear_catalog,
    create_book,
    create_category,
    delete_book,
    get_books,
    get_categories,
    update_book_price,
    update_category_name,
)
from app.db import SessionLocal, create_tables


def prepare_catalog() -> None:
    create_tables()

    session = SessionLocal()

    try:
        clear_catalog(session)

        study = create_category(session, "учебная литература")
        code = create_category(session, "программирование")
        stories = create_category(session, "современная проза")
        draft = create_category(session, "временный раздел")

        update_category_name(session, draft.id, "архивные записи")

        book_python = create_book(
            session,
            title="python: первые проекты",
            description="Книга с простыми примерами для закрепления основ Python.",
            price=730.00,
            url="https://example.com/python-first-projects",
            category_id=code.id,
        )

        create_book(
            session,
            title="postgresql на практике",
            description="Материал о таблицах, связях и базовых операциях с данными.",
            price=860.00,
            url="https://example.com/postgresql-practice",
            category_id=study.id,
        )

        create_book(
            session,
            title="sqlalchemy для небольшого приложения",
            description="Краткое руководство по моделям, сессиям и CRUD.",
            price=990.00,
            url="https://example.com/sqlalchemy-small-app",
            category_id=code.id,
        )

        create_book(
            session,
            title="город тихих окон",
            description="Художественная книга, добавленная как пример записи.",
            price=520.00,
            url="https://example.com/quiet-windows",
            category_id=stories.id,
        )

        removed_book = create_book(
            session,
            title="техническая запись",
            description="Эта книга создана для проверки удаления.",
            price=100.00,
            url="https://example.com/service-row",
            category_id=draft.id,
        )

        update_book_price(session, book_python.id, 750.00)
        delete_book(session, removed_book.id)

        print("подготовка базы данных завершена")
        print(f"категорий добавлено: {len(get_categories(session))}")
        print(f"книг осталось после проверки CRUD: {len(get_books(session))}")

    finally:
        session.close()


if __name__ == "__main__":
    prepare_catalog()
