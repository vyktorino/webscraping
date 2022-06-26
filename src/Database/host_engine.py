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

# class ClassTweet(Base):
#     __tablename__ = "tweets"

#     id = Column(String, primary_key=True)
#     date = Column(String)
#     place = Column(String)
#     tweet = Column(String)

#     def __repr__(self):
#         return "<ClassTweet(date = '%s', place = '%s', tweet = '%s'" % (
#             self.date,
#             self.place,
#             self.tweet,
#         )


# if __name__ == "__main__":
#     print(Base.metadata.create_all(engine))
