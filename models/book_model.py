from sqlalchemy import String,Integer,Column,Date
from db.database import Base

class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer,primary_key=True)
    title = Column(String(255),nullable=False)
    author = Column(String(255),nullable=False)
    publisher = Column(String(255))
    published_date = Column(Date)
    page_count=Column(Integer)
    language = Column(String(50))