from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database URL and create the engine
DATABASE_URL = 'sqlite:///database.db'
engine = create_engine(DATABASE_URL)

# Define metadata and Base without binding to the engine
metadata = MetaData()
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

# Create tables by binding the engine at this stage
Base.metadata.create_all(bind=engine)

# Start local session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Add sample users to the database
sample_users = [
    {"id": 1, "username": "Khumalo_Kat", "password": "password1"},
    {"id": 2, "username": "MV_Sibanyoni", "password": "password2"},
]

for user_data in sample_users:
    user = User(id=user_data["id"], username=user_data["username"], password=user_data["password"])
    session.add(user)

# Commit the session and close it
session.commit()
session.close()

print("Sample users added to the database.")
