from sqlalchemy.orm import Session

from app.models import Book, Category


def clear_catalog(session: Session) -> None:
    session.query(Book).delete()
    session.query(Category).delete()
    session.commit()


def create_category(session: Session, title: str) -> Category:
    category = Category(title=title)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


def get_categories(session: Session) -> list[Category]:
    return session.query(Category).order_by(Category.id).all()


def update_category_name(
    session: Session,
    category_id: int,
    new_title: str,
) -> Category | None:
    category = session.query(Category).filter(Category.id == category_id).first()

    if category is None:
        return None

    category.title = new_title
    session.commit()
    session.refresh(category)
    return category


def delete_category(session: Session, category_id: int) -> bool:
    category = session.query(Category).filter(Category.id == category_id).first()

    if category is None:
        return False

    session.delete(category)
    session.commit()
    return True


def create_book(
    session: Session,
    title: str,
    description: str,
    price: float,
    url: str,
    category_id: int,
) -> Book:
    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id,
    )

    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def get_books(session: Session) -> list[Book]:
    return session.query(Book).order_by(Book.id).all()


def update_book_price(
    session: Session,
    book_id: int,
    new_price: float,
) -> Book | None:
    book = session.query(Book).filter(Book.id == book_id).first()

    if book is None:
        return None

    book.price = new_price
    session.commit()
    session.refresh(book)
    return book


def delete_book(session: Session, book_id: int) -> bool:
    book = session.query(Book).filter(Book.id == book_id).first()

    if book is None:
        return False

    session.delete(book)
    session.commit()
    return True
