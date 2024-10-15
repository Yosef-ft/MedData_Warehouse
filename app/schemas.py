from typing import *
import datetime
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    pass

class Product(BaseModel):
    id: Optional[int] = Field(None, alias="ID") 
    price: Optional[int] = Field(None, alias="Price") 
    Product: str
    Tellno: str
    Address: str

    class Config:
        from_attributes=True

class Telegram(BaseModel):
    id: Optional[int] = Field(None, alias="ID") 
    Date : str
    Channel_username: str
    Media_path : str
    Message: Optional[str] = Field(None, alias="Message") 

    class Config:
        from_attributes=True

class Detected_Images(BaseModel):
    id: Optional[int] = Field(None, alias="ID") 
    label: str
    confidence: float
    Image : str
    x_max : float 
    x_min : float 
    y_max : float 
    y_min : float