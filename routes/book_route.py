from fastapi import APIRouter,HTTPException,status
from typing import List

from data.books_data import books
from schemas.book_schema import Book,UpdateBook

book_router=APIRouter()

@book_router.get("/books",response_model=List[Book])
def get_all_books():
    return books

@book_router.post("/books",status_code=status.HTTP_201_CREATED)
def create_a_book(book_data:Book):
    if any(book["id"] == book_data.id for book in books):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Book with this ID already exists"
        )
    books.append(book_data.model_dump())    
    return book_data

@book_router.get("/books/{book_id}",response_model=Book)
def get_a_book(book_id:int)->Book:
    for book in books:
        if book['id']==book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )

@book_router.patch("/books/{book_id}",response_model=Book)
def update_a_book(book_id:int,update_book:UpdateBook)->Book:
    for book in books:
        if book['id']==book_id:
            for key,value in update_book.model_dump(exclude_unset=True).items():
                book[key]=value
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )

@book_router.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_a_book(book_id:int):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return 

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


