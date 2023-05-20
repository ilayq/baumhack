from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class CityORM(Base):
    __tablename__ = 'cities'

    date = Column(Date, nullable=False, primary_key=True)
    city_name = Column(String, nullable=False, primary_key=True)
    state = Column(String, nullable=False, primary_key=True)
    all_covid_accidents = Column(Integer, nullable=False)
    new_accidents = Column(Integer, nullable=False)
    lethal_accidents = Column(Integer, nullable=False)
