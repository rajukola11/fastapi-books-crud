from pydantic import BaseModel
from typing import Optional
from datetime import date

class Book(BaseModel):
    id:int
    title:str
    author:str
    publisher:str
    published_date:date
    page_count:int
    language:str

class UpdateBook(BaseModel):
    title:Optional[str]=None
    author:Optional[str]=None
    publisher:Optional[str]=None
    language:Optional[str]=None
