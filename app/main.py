from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    init_db()

app = FastAPI(lifespan=lifespan)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/cars/", response_model=schemas.Car)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = crud.get_car(db, name=car.name)
    if db_car:
        raise HTTPException(status_code=400, detail="Car already registered")
    return crud.create_car(db=db, car=car)

@app.get("/cars/{name}", response_model=schemas.Car)
def read_car(name: str, db: Session = Depends(get_db)):
    db_car = crud.get_car(db, name=name)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@app.get("/cars/", response_model=list[schemas.Car])
def read_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cars = crud.get_cars(db, skip=skip, limit=limit)
    return cars

@app.put("/cars/{power}", response_model=schemas.Car)
def update_car(power: str, car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = crud.get_car_by_power(db, power=power)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return crud.update_car(db=db, power=power, car=car)

@app.delete("/cars/{name}", response_model=schemas.Car)
def delete_car(name: str, db: Session = Depends(get_db)):
    db_car = crud.get_car(db, name=name)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return crud.delete_car(db=db, name=name)
