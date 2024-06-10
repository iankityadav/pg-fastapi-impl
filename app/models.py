from sqlalchemy import Column, String
from .database import Base

class Car(Base):
    __tablename__ = 'cars'
    
    brand = Column(String, index=True)
    name = Column(String, index=True, primary_key=True)
    color = Column(String)
    power = Column(String)
    safety_ratings = Column(String)
