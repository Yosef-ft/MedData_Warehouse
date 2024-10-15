from sqlalchemy import Column, Integer, Text, TIMESTAMP, BIGINT, String, FLOAT
from database import Base

class Products(Base):
    __tablename__ = "Products"

    ID = Column(BIGINT, primary_key=True)
    Product = Column(Text)
    Price = Column(Text)
    Address = Column(Text)
    Tellno = Column(Text)


class Telegram(Base):
    __tablename__ = "Telegram"

    Channel_username = Column(Text)
    Date = Column(String)
    Media_path = Column(Text)
    Message = Column(Text)
    ID = Column(BIGINT, primary_key=True)
    

class Detected_Images(Base):

    __tablename__ = "detected_images"

    Image = Column(String)
    ID = Column(BIGINT, primary_key=True)
    label = Column(String)
    confidence = Column(BIGINT)
    x_max = Column(FLOAT)
    x_min = Column(FLOAT)
    y_max = Column(FLOAT)
    y_min = Column(FLOAT)
