from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Variant(Base):
    __tablename__ = 'variants'
    VariantId = Column(Integer, primary_key=True, autoincrement=True)
    GeneId = Column(String, ForeignKey('genes.GeneId'), nullable=False)
    VariantType = Column(String, nullable=False)
    ReferenceAlleleName = Column(String, nullable=False)
    AlleleName = Column(String, nullable=False, unique=True)
    NucleotideChange = Column(String, nullable=False)
    GenomicStart = Column(Integer)
    GenomicEnd = Column(Integer)
    gene = relationship("Gene", back_populates="variants")
    alleles = relationship("Allele", back_populates="variant")
