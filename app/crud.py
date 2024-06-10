from sqlalchemy.orm import Session
from . import models, schemas

def get_car(db: Session, name: str):
    return db.query(models.Car).filter(models.Car.name == name).first()

def get_car_by_power(db: Session, power: str):
    return db.query(models.Car).filter(models.Car.power == power).first()

def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Car).offset(skip).limit(limit).all()

def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(
        brand=car.brand,
        name=car.name,
        color=car.color,
        power=car.power,
        safety_ratings=car.safety_ratings
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def update_car(db: Session, power: str, car: schemas.CarCreate):
    db_car = db.query(models.Car).filter(models.Car.power == power).first()
    if db_car:
        db_car.name = car.name
        db_car.color = car.color
        db_car.power = car.power
        db_car.safety_ratings = car.safety_ratings
        db.commit()
        db.refresh(db_car)
    return db_car

def delete_car(db: Session, name: str):
    db_car = db.query(models.Car).filter(models.Car.name == name).first()
    if db_car:
        db.delete(db_car)
        db.commit()
    return db_car
