from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import List

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

@app.get("/books",response_model=List[Book])
def get_all_books():
    return books

@app.post("/book",status_code=status.HTTP_201_CREATED)
def create_a_book(book_data:Book)->dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get("/book/{book_id}",response_model=Book)
def get_a_book(book_id:int)->dict:
    for book in books:
        if book['id']==book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )

    