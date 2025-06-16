from sqlalchemy import Column, Integer, String
from infrastructure.database import Base

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(127), index=True, nullable=False)
    description = Column(String(511))
    phone = Column(String(20), index=True)
    email = Column(String(127), unique=True, index=True, nullable=False)
    address = Column(String(255), index=True)