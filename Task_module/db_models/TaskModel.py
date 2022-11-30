from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .Base import Base


class Task(Base):
    __tablename__ = "Task"

    id_ = Column(Integer, primary_key=True)
    description = Column(String)
    create_time = Column(DateTime)
    destination_time = Column(DateTime)
    previous_time = Column(DateTime)

    owner_id = relationship("Person.id_")
    importance_level_id = relationship("TaskImportance.id_") ###########
    status_id = relationship("TaskStatus.id_") ##############
