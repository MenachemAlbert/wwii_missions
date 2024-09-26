from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from config.base import Base


class Target(Base):
    __tablename__ = 'targets'

    target_id = Column(Integer, primary_key=True, autoincrement=True)
    locations_id = Column(Integer, ForeignKey('locations.location_id'), nullable=False)
    target_type_id = Column(Integer, ForeignKey('target_types.target_type_id'))
    industry_id = Column(Integer, ForeignKey('industry.industry_id'))
    target_priority = Column(Integer, nullable=False)

    location = relationship('Location', back_populates='targets')
    target_type = relationship('TargetType', back_populates='targets')
    industry = relationship('Industry', back_populates='targets')
