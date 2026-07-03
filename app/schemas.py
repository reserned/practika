from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    title: str = Field(min_length=2, max_length=120)


class CategoryUpdate(BaseModel):
    title: str = Field(min_length=2, max_length=120)


class CategoryOut(BaseModel):
    id: int
    title: str


class BookCreate(BaseModel):
    title: str = Field(min_length=2, max_length=180)
    description: str = Field(min_length=5)
    price: float = Field(gt=0)
    url: str = ""
    category_id: int


class BookUpdate(BaseModel):
    title: str = Field(min_length=2, max_length=180)
    description: str = Field(min_length=5)
    price: float = Field(gt=0)
    url: str = ""
    category_id: int


class BookOut(BaseModel):
    id: int
    title: str
    description: str
    price: float
    url: str
    category_id: int
    category: CategoryOut | None = None
