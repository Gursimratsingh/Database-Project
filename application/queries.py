from database.database import Session
from models.gene import Gene
from models.variant import Variant
from models.allele import Allele

def query_nucleotide_changes_for_allele(allele_name):
    session = Session()
    result = session.query(Variant.NucleotideChange).filter(Variant.AlleleName == allele_name).all()
    session.close()
    return result

def query_alleles_on_chromosome_between_positions(chromosome_id, start_position, end_position):
    session = Session()
    count = session.query(Variant).filter(
        Variant.GeneId == chromosome_id,
        Variant.GenomicStart >= start_position,
        Variant.GenomicEnd <= end_position
    ).count()
    session.close()
    return count

def query_phenotypes_with_multiple_nucleotide_changes():
    session = Session()
    count = session.query(Variant).filter(Variant.NucleotideChange.like('%;%')).count()
    session.close()
    return count
