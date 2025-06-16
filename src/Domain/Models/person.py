import uuid
from sqlalchemy import Column, Integer, String
from src.Infrastructure.database import Base
from sqlalchemy.dialects.postgresql import UUID

class Person(Base):
    __tablename__ = "persons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(127), index=True, nullable=False)
    description = Column(String(511))
    phone = Column(String(20), index=True)
    email = Column(String(127), unique=True, index=True, nullable=False)
    address = Column(String(255), index=True)
