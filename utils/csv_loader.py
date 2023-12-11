import pandas as pd
from models.gene import Gene
from models.variant import Variant
from models.allele import Allele

def load_csv(file_path):
    return pd.read_csv(file_path)

def process_data(df, session):
    for _, row in df.iterrows():
        # Ensure the gene exists in the database or create it
        gene_id = row['GeneId']
        gene = session.query(Gene).filter_by(GeneId=gene_id).first()
        if not gene:
            gene = Gene(GeneId=gene_id, GeneName=row['GeneName'])
            session.add(gene)
            session.commit()

        # Create and add the variant
        variant = Variant(
            GeneId=gene.GeneId,
            VariantType=row['VariantType'],
            ReferenceAlleleName=row['ReferenceAlleleName'],
            AlleleName=row['AlleleName'],
            NucleotideChange=row['NucleotideChange'],
            GenomicStart=row['GenomicStart'],
            GenomicEnd=row['GenomicEnd']
        )
        session.add(variant)

        try:
            session.commit()
        except IntegrityError:
            # Handle cases where a duplicate entry might be attempted
            session.rollback()
            continue

        # Split and add alleles
        ref_alleles = row['ReferenceAllele'].split('|')
        alt_alleles = row['AlternateAllele'].split('|')
        for ref_allele, alt_allele in zip(ref_alleles, alt_alleles):
            allele = Allele(
                VariantId=variant.VariantId,
                ReferenceAllele=ref_allele.strip(),
                AlternateAllele=alt_allele.strip()
            )
            session.add(allele)

        try:
            session.commit()
        except IntegrityError:
            session.rollback()