from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud
from app.db import get_db
from app.schemas import CategoryCreate, CategoryOut, CategoryUpdate


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


def pack_category(category) -> dict:
    return {
        "id": category.id,
        "title": category.title,
    }


@router.get("/", response_model=list[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    categories = crud.get_categories(db)
    return [pack_category(category) for category in categories]


@router.get("/{category_id}", response_model=CategoryOut)
def get_one_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="category not found",
        )

    return pack_category(category)


@router.post("/", response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
def add_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    try:
        category = crud.create_category(db, payload.title)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="category already exists",
        )

    return pack_category(category)


@router.put("/{category_id}", response_model=CategoryOut)
def edit_category(
    category_id: int,
    payload: CategoryUpdate,
    db: Session = Depends(get_db),
):
    same_title = crud.get_category_by_title(db, payload.title)

    if same_title is not None and same_title.id != category_id:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="category title already used",
        )

    category = crud.update_category_name(
        db,
        category_id=category_id,
        new_title=payload.title,
    )

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="category not found",
        )

    return pack_category(category)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_category(category_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_category(db, category_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="category not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
