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


def get_category(session: Session, category_id: int) -> Category | None:
    return session.query(Category).filter(Category.id == category_id).first()


def get_category_by_title(session: Session, title: str) -> Category | None:
    return session.query(Category).filter(Category.title == title).first()


def update_category_name(
    session: Session,
    category_id: int,
    new_title: str,
) -> Category | None:
    category = get_category(session, category_id)

    if category is None:
        return None

    category.title = new_title
    session.commit()
    session.refresh(category)
    return category


def delete_category(session: Session, category_id: int) -> bool:
    category = get_category(session, category_id)

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


def get_books(
    session: Session,
    category_id: int | None = None,
) -> list[Book]:
    query = session.query(Book).order_by(Book.id)

    if category_id is not None:
        query = query.filter(Book.category_id == category_id)

    return query.all()


def get_book(session: Session, book_id: int) -> Book | None:
    return session.query(Book).filter(Book.id == book_id).first()


def update_book(
    session: Session,
    book_id: int,
    title: str,
    description: str,
    price: float,
    url: str,
    category_id: int,
) -> Book | None:
    book = get_book(session, book_id)

    if book is None:
        return None

    book.title = title
    book.description = description
    book.price = price
    book.url = url
    book.category_id = category_id

    session.commit()
    session.refresh(book)
    return book


def update_book_price(
    session: Session,
    book_id: int,
    new_price: float,
) -> Book | None:
    book = get_book(session, book_id)

    if book is None:
        return None

    book.price = new_price
    session.commit()
    session.refresh(book)
    return book


def delete_book(session: Session, book_id: int) -> bool:
    book = get_book(session, book_id)

    if book is None:
        return False

    session.delete(book)
    session.commit()
    return True
