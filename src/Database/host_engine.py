import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# connecting
engine = create_engine('sqlite:///:memory:', echo=True)

# declare mapping
Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweets'
    
    