from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

# Database file
DATABASE_FILE = 'sqlite:///data/_genes_data.db'

engine = create_engine(DATABASE_FILE)
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)
