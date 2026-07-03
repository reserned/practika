import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from app.crud import get_books, get_categories
from app.db import SessionLocal


def show_database_content() -> None:
    session = SessionLocal()

    try:
        categories = get_categories(session)
        books = get_books(session)

        print("список категорий:")
        for category in categories:
            print(f"{category.id}) {category.title}")

        print()
        print("список книг:")

        for book in books:
            print(f"{book.id}) {book.title}")
            print(f"   категория: {book.category.title}")
            print(f"   цена: {book.price} руб.")
            print(f"   описание: {book.description}")
            print(f"   ссылка: {book.url}")
            print()

    finally:
        session.close()


if __name__ == "__main__":
    show_database_content()
