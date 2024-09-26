from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from config.base import Base


class Location(Base):
    __tablename__ = 'locations'

    location_id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float)
    longitude = Column(Float)
    city_id = Column(Integer, ForeignKey('cities.city_id'), nullable=False)

    cities = relationship('City', back_populates='location')
    targets = relationship('Target', back_populates='location')
