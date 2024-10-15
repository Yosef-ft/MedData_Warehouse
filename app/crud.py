from sqlalchemy.orm import Session
import models, schemas
from models import Telegram

def get_items(model, db: Session, limit: int= 10):

    if model == Telegram:
        telegrams = db.query(Telegram).limit(limit).all()

        for telegram in telegrams:
            telegram.Date = str(telegram.Date)

        return telegrams

    return db.query(model).limit(limit).all()
