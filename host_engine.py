import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# connecting
engine = create_engine(
    r"sqlite:///C:\Users\space\nebula\webscraping\engine.db", echo=True
)

# declare mapping
Base = declarative_base()
