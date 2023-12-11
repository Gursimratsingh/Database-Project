# Blood Type Variant Database

## Overview

This project creates and populates a SQLite database with blood type variant data extracted 
from the International Society for Blood Transfusion. It includes a set of Python scripts to 
load data from a CSV file into a structured database and provides functionalities to query 
specific data based on various criteria.

## Project Structure

- `main.py`: The main script that orchestrates the data loading and querying processes.
- `application/`
  - `queries.py`: Contains functions to execute specific database queries.
- `models/`
  - `gene.py`: Contains the Gene model.
  - `variant.py`: Contains the Variant model.
  - `allele.py`: Contains the Allele model.
  - `base.py`: Contains the SQLAlchemy Base object.
- `utils/`
  - `csv_loader.py`: Responsible for loading and processing data from the CSV file.
- `database/`
  - `database.py`: Manages the database connection and session creation.
- `data/`
  - `your_database_file.db`: SQLite database file (this will be created when you run the application).

## Setup

### Requirements

- Python 3.x
- SQLite
- Libraries: SQLAlchemy, Pandas

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Gursimratsingh/Database-Project.git
```
2. Navigate to the project directory:
```bash
cd [your-project-directory]
```
3. Create a Virtual environment for python (optional)
```bash
python -m venv .venv
```
4. Activate the newly created venv (optional)
```bash
.\.venv\Scripts\activate.ps1
```
5. Install the required Python packages:
```bash
pip install -r requirements.txt
```
### Database Initialization

Run `main.py` to initialize the database and populate it with data from the provided CSV file:

python main.py


## Usage

To query the database, you can use the functions provided in `queries.py`. Example usage in a Python script:

```python
from queries import query_nucleotide_changes_for_allele

# Example query
result = query_nucleotide_changes_for_allele('RHCE*Ce.10.02')
print(result)


## Note:
This  is a software based project. I have also added "DataTest.py" file for your reference
 that will run the database queries as per asked in the question. Let me know if you need help. 

## Solutions:
The database consists of three tables:
- Genes: Stores information about genes (GeneID, GeneName).
- Variants: Stores information about variants (VariantID, GeneID, VariantType, NucleotideChange,
ReferenceAllele, AlternateAllele, GenomicStart, GenomicEnd).
- Alleles: Stores information about alleles (AlleleID, AlleleName, VariantID).
This structure allows efficient querying based on genes, variants, and alleles.

-> Example Queries and Results

Query 1: Nucleotide changes for allele RHCE*Ce.10.02
Result: No data found for this specific allele in the database.

Query 2: Count alleles on chromosome 1 between positions 25362249 and 25430203
Result: 0 (No alleles found within this specific genomic range for the RHCE gene).

Query 3: Count phenotypes with multiple nucleotide changes
Result: 42 (Indicates the number of distinct alleles with multiple nucleotide changes).
