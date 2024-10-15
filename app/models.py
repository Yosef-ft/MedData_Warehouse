from sqlalchemy import Column, Integer, Text, TIMESTAMP, BIGINT, String, FLOAT, DateTime
from database import Base

class Products(Base):
    __tablename__ = "Products"

    ID = Column(BIGINT, primary_key=True, index=True)
    Product = Column(Text, index=True)
    Price = Column(Text, index=True)
    Address = Column(Text, index=True)
    Tellno = Column(Text, index=True)


class Telegram(Base):
    __tablename__ = "Telegram"

    Channel_username = Column(Text)
    Date = Column(DateTime)
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
