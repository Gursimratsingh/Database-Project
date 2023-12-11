from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Allele(Base):
    __tablename__ = 'alleles'
    AlleleId = Column(Integer, primary_key=True, autoincrement=True)
    VariantId = Column(Integer, ForeignKey('variants.VariantId'), nullable=False)
    ReferenceAllele = Column(String, nullable=False)
    AlternateAllele = Column(String, nullable=False)
    variant = relationship("Variant", back_populates="alleles")
