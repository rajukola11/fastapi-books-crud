from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from typing import List

from schemas.book_schema import Book,UpdateBook
from models.book_model import BookModel
from db.deps import get_db

book_router=APIRouter()

@book_router.get("/books",response_model=List[Book])
def get_all_books(db:Session=Depends(get_db)):
    books = db.query(BookModel).all()
    return books

@book_router.post("/books",status_code=status.HTTP_201_CREATED)
def create_a_book(book_data:Book,db:Session=Depends(get_db)):
    existing = db.query(BookModel).filter(BookModel.id == book_data.id).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Book with this ID already exists"
        )
    new_book = BookModel(**book_data.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@book_router.get("/books/{book_id}",response_model=Book)
def get_a_book(book_id:int,db:Session=Depends(get_db))->Book:
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return book

@book_router.patch("/books/{book_id}",response_model=Book)
def update_a_book(book_id:int,update_book:UpdateBook,db:Session=Depends(get_db))->Book:
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    for key,value in update_book.model_dump(exclude_unset=True).items():
        setattr(book,key,value)
    db.commit()
    db.refresh(book)
    return book

@book_router.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_a_book(book_id:int,db:Session=Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    db.delete(book)
    db.commit()
    return 


