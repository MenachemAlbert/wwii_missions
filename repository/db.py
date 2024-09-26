from config.base import Base, engine


def create_tables():
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print(e)


def drop_tables():
    Base.metadata.drop_all(engine)
