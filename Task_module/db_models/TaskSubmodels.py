from sqlalchemy import Column, Integer, String

from Task_module.db_models import Base


class TaskImportance(Base):
    __tablename__ = "TaskImportance"

    id_ = Column(Integer, primary_key=True)
    name = Column(String)


class TaskStatus(Base):
    __tablename__ = "TaskStatus"

    id = Column(Integer, primary_key=True)
    name = Column(String)