import sqlite3
import pandas as pd

# Read the CSV file
file_name = 'data.csv'  # CSV File
data = pd.read_csv(file_name)

# Connect to the SQLite database
conn = sqlite3.connect('blood_cell_genotyping.db')
cursor = conn.cursor()

# Create table for alleles
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alleles (
        AlleleID INTEGER PRIMARY KEY,
        GeneName TEXT,
        GeneID TEXT,
        VariantType TEXT,
        ReferenceAlleleName TEXT,
        AlleleName TEXT,
        ReferenceAllele TEXT,
        AlternateAllele TEXT,
        NucleotideChange TEXT,
        GenomicStart INTEGER,  -- Modify column names as needed
        GenomicEnd INTEGER  -- Modify column names as needed
    )
''')

# Insert data into the database
data.to_sql('Alleles', conn, if_exists='replace', index=False)

# Query 1: What are the nucleotide changes for allele RHCE*Ce.10.02?
cursor.execute('''
    SELECT NucleotideChange
    FROM Alleles
    WHERE AlleleName = 'RHCE*Ce.10.02'
''')
result_1 = cursor.fetchall()
print("Nucleotide changes for allele RHCE*Ce.10.02:", result_1)

# Query 2: How many alleles documented in the database are positioned on chromosome 1 between position 25362249 and 25430203?
cursor.execute('''
    SELECT COUNT(*)
    FROM Alleles
    WHERE GeneName = 'Chromosome 1' 
    AND GenomicStart >= 25362249 
    AND GenomicEnd <= 25430203
''')
result_2 = cursor.fetchone()[0]
print("Number of alleles on Chromosome 1 between positions 25362249 and 25430203:", result_2)

# Query 3: How many phenotypes carry multiple nucleotide changes?
cursor.execute('''
    SELECT COUNT(DISTINCT AlleleName)
    FROM Alleles
    WHERE AlternateAllele LIKE '%|%'
''')
result_3 = cursor.fetchone()[0]
print("Number of phenotypes carrying multiple nucleotide changes:", result_3)

# Commit changes and close connection
conn.commit()
conn.close()