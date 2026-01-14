from fastapi import FastAPI
from routes.book_route import book_router


app = FastAPI()

app.include_router(book_router)

