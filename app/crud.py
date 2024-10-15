from sqlalchemy.orm import Session
import models, schemas
from models import Telegram, Products

def get_items(model, db: Session, limit: int= 10):

    if model == Telegram:
        telegrams = db.query(Telegram).limit(limit).all()

        for telegram in telegrams:
            telegram.Date = str(telegram.Date)

        return telegrams

    return db.query(model).limit(limit).all()


def get_item(model, db: Session, item_id):
    
    if model == Telegram:
        telegram = db.query(model).filter(model.ID == item_id).first()
        telegram.Date = str(telegram.Date)

        return telegram
    
    return db.query(model).filter(model.ID == item_id).first()
