from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///task_scheduler_v1.db', echo=True)
Base = declarative_base()
