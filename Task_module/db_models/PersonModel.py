from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base


class Person(Base):
    __tablename__ = 'Person'

    id_ = Column(Integer, primary_key=True) # try adding backref
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    informer_id = relationship('PersonInformer.id_', backref='PersonInformer.id')  # check this
    status_id = relationship('PersonStatus.id_', backref='PersonStatus.id')
