from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, get_db
from models import Telegram, Products, Detected_Images

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Below are 3 endpoints to get items
@app.get('/products/', response_model=list[schemas.Product])
def read_products(limit: int=10, db: Session = Depends(get_db)):
    products = crud.get_items(Products, db, limit=limit)
    return products

@app.get('/telegram/', response_model= list[schemas.Telegram])
def read_telegram_datas(limit: int=10, db: Session = Depends(get_db)):
    telegram = crud.get_items(Telegram, db, limit=limit)
    return telegram

@app.get('/detected-images/', response_model= list[schemas.Detected_Images])
def read_detected_images(limit: int =10, db: Session = Depends(get_db)):
    detected_images = crud.get_items(Detected_Images, db, limit=limit)
    return detected_images



# Below are 3 endpoints to get items by id
@app.get('/products/{item_id}', response_model=schemas.Product)
def read_product(item_id: int, db: Session = Depends(get_db)):
    product = crud.get_item_by_id(Products, db, item_id=item_id)
    return product

@app.get('/telegram/{item_id}', response_model=schemas.Telegram)
def read_telegram_data(item_id: int, db:Session = Depends(get_db)):
    telegram = crud.get_item_by_id(Telegram, db, item_id=item_id)
    return telegram

@app.get('/detected-images/{item_id}', response_model= schemas.Detected_Images)
def read_detected_image(item_id: int, db: Session = Depends(get_db)):
    image = crud.get_item_by_id(Detected_Images, db, item_id=item_id)
    return image


# Below are endpoints to create items
@app.post('/products/', response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_item(Products, db=db, item=product)

@app.post('/telegram/', response_model=schemas.Telegram)
def create_telegram(telegram: schemas.TelegramCreate, db: Session = Depends(get_db)):
    return crud.create_item(Telegram, db=db, item=telegram)

@app.post('/detected-images/', response_model= schemas.Detected_Images)
def create_image(image: schemas.Detected_Image_Create, db: Session = Depends(get_db)):
    return crud.create_item(Detected_Images, db=db, item=image)


# Below are endpoint to delete items
@app.delete('/products/{item_id}', response_model=schemas.Product)
def delete_product(item_id: int, db: Session = Depends(get_db)):
    item = crud.delete_item(Products, db=db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return item


@app.delete('/telegram/{item_id}', response_model=schemas.Telegram)
def delete_product(item_id: int, db: Session = Depends(get_db)):
    item = crud.delete_item(Telegram, db=db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Telegram ID not found")
    return item


@app.delete('/detected-images/{item_id}', response_model=schemas.Detected_Images)
def delete_product(item_id: int, db: Session = Depends(get_db)):
    item = crud.delete_item(Detected_Images, db=db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Detected image ID not found")
    return item
    