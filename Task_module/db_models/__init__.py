from Task_module.db_models.Base import Base, engine


def create_db():
    Base.metadata.create_all(engine)