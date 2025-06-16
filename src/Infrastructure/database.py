from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:QWERTY12345@localhost:5432/python_lab"

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
