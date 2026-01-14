from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import List,Optional

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-01",
        "page_count": 464,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "published_date": "2022-04-01",
        "page_count": 1014,
        "language": "English",
    },
    {
        "id": 4,
        "title": "You Don't Know JS Yet",
        "author": "Kyle Simpson",
        "publisher": "Independently published",
        "published_date": "2020-01-28",
        "page_count": 143,
        "language": "English",
    },
]

class Book(BaseModel):
    id:int
    title:str
    author:str
    publisher:str
    published_date:str
    page_count:int
    language:str

class UpdateBook(BaseModel):
    title:Optional[str]=None
    author:Optional[str]=None
    publisher:Optional[str]=None
    language:Optional[str]=None

@app.get("/books",response_model=List[Book])
def get_all_books():
    return books

@app.post("/book",status_code=status.HTTP_201_CREATED)
def create_a_book(book_data:Book):
    if any(book["id"] == book_data.id for book in books):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Book with this ID already exists"
        )
    books.append(book_data.model_dump())    
    return book_data

@app.get("/book/{book_id}",response_model=Book)
def get_a_book(book_id:int)->Book:
    for book in books:
        if book['id']==book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )

@app.patch("/book/{book_id}",response_model=Book)
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

@app.delete("/book/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_a_book(book_id:int):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return 

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


