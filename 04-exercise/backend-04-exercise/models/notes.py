from config.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String

class Note(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="notes_id")