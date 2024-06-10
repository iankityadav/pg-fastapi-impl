from pydantic import BaseModel

class CarBase(BaseModel):
    brand: str
    color: str
    power: str
    safety_ratings: str

class CarCreate(CarBase):
    name: str

class Car(CarBase):
    name: str

    class Config:
        orm_mode = True
