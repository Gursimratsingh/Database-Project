from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base import Base

class Gene(Base):
    __tablename__ = 'genes'
    GeneId = Column(String, primary_key=True)
    GeneName = Column(String, nullable=False)
    variants = relationship("Variant", back_populates="gene")
