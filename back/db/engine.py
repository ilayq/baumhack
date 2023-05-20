from sqlalchemy import create_engine


engine = create_engine("sqlite:///db.db")


if __name__ == '__main__':
    from models import Base

    Base.metadata.create_all(bind=engine)
