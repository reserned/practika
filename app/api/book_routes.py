from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app import crud
from app.db import get_db
from app.schemas import BookCreate, BookOut, BookUpdate


router = APIRouter(
    prefix="/books",
    tags=["books"],
)


def pack_book(book) -> dict:
    return {
        "id": book.id,
        "title": book.title,
        "description": book.description,
        "price": float(book.price),
        "url": book.url,
        "category_id": book.category_id,
        "category": {
            "id": book.category.id,
            "title": book.category.title,
        } if book.category else None,
    }


@router.get("/", response_model=list[BookOut])
def list_books(
    category_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    if category_id is not None:
        category = crud.get_category(db, category_id)

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="category for filter not found",
            )

    books = crud.get_books(db, category_id=category_id)
    return [pack_book(book) for book in books]


@router.get("/{book_id}", response_model=BookOut)
def get_one_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="book not found",
        )

    return pack_book(book)


@router.post("/", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def add_book(payload: BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, payload.category_id)

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="cannot create book without existing category",
        )

    book = crud.create_book(
        db,
        title=payload.title,
        description=payload.description,
        price=payload.price,
        url=payload.url,
        category_id=payload.category_id,
    )

    return pack_book(book)


@router.put("/{book_id}", response_model=BookOut)
def edit_book(
    book_id: int,
    payload: BookUpdate,
    db: Session = Depends(get_db),
):
    category = crud.get_category(db, payload.category_id)

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="cannot move book to missing category",
        )

    book = crud.update_book(
        db,
        book_id=book_id,
        title=payload.title,
        description=payload.description,
        price=payload.price,
        url=payload.url,
        category_id=payload.category_id,
    )

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="book not found",
        )

    return pack_book(book)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_book(book_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_book(db, book_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="book not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
