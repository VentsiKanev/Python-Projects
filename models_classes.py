# models_classes.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

# --- Base class ---
Base = declarative_base()

# --- Define your table as a class ---
class Person(Base):
    __tablename__ = "person"  # match your table name exactly

    # Columns
    person_id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    diary_entry = Column(Text, nullable=False)

    # Constructor (optional, you can also just use Person(...))
    def __init__(self, first_name, last_name, diary_entry):
        self.first_name = first_name
        self.last_name = last_name
        self.diary_entry = diary_entry

    # Helper method to convert object to dictionary
    def to_dict(self):
        return {
            "id": self.person_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "diary_log": self.diary_entry
        }
    # makes print output human-readable
    def __repr__(self):
        return f"<Person(id={self.person_id}, name={self.first_name} {self.last_name})>"

