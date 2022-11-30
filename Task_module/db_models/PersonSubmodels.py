from sqlalchemy import Column, Integer, String
from .Base import Base


class PersonStatus(Base):
    __tablename__ = "PersonStatus"

    id_ = Column(Integer, primary_key=True)  # try adding backref
    name = Column(String, nullable=False)


class PersonInformer(Base):
    __tablename__ = "PersonInformer"

    id_ = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

