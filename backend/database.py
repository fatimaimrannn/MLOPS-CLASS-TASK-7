from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base model for SQLAlchemy
Base = declarative_base()

# User table schema
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

# Create SQLite engine
DATABASE_URL = "sqlite:///users.db"  # SQLite database in the backend folder
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(engine)

# Session maker for database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
