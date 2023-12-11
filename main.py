from database.database import create_tables, Session
from utils.csv_loader import load_csv, process_data
import application.queries as queries 

def main():
    # Create database tables
    create_tables()

    # Load and process CSV data
    file_path = 'data/data.csv'
    df = load_csv(file_path)

    # Insert data into the database
    session = Session()
    process_data(df, session)
    session.close()

    print("Data insertion process completed.")

    # Example queries
    print("Query results:")
    print("Nucleotide changes for allele RHCE*Ce.10.02:", queries.query_nucleotide_changes_for_allele('RHCE*Ce.10.02'))
    print("Alleles on chromosome 1 between positions 25362249 and 25430203:", queries.query_alleles_on_chromosome_between_positions('ENSG00000188672', 25362249, 25430203))
    print("Phenotypes with multiple nucleotide changes:", queries.query_phenotypes_with_multiple_nucleotide_changes())

if __name__ == "__main__":
    main()
