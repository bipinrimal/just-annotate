import sys
import argparse
from pony.orm import *
import csv
from itertools import *
import time
import sqlite3

# Parse arguments
parser=argparse.ArgumentParser(description="Create sqlite3 annotation database combining gene to geneontology table and gene to gene to accession table.")
parser.add_argument("-db","--database",help="Name of the database file")
parser.add_argument("-g","--gene_go",help="File with GO terms associated with Genes in Entrez Gene.")
parser.add_argument("-p","--gene_acc",help="File with accessions that are related to GeneID.")
args=parser.parse_args()

dbname=str(args.database)
gene_go=str(args.gene_go)
gene_acc=str(args.gene_acc)

################################################################################

#Create database and tables and map them

db = Database("sqlite", str(args.database), create_db=True)

class Gene2go(db.Entity):
    """
    Pony ORM Model for Genetogo table containing protein accession link, go-term, go-id and go category
    """
    geneid = Required(str, index="geneid")
    go_term = Required(str, index="go_term")
    go_id = Required(str, index="go_id")
    category = Required(str, index="category")

class Gene2acc(db.Entity):
    """
    Pony ORM model for Protein accession table containing protein accession, gene symbol and gene_did
    """
    prot_acc = Required(str, index="prot_acc")
    symbol = Required(str, index="symbol")
    gene_id = Required(str, index="gene_id")


# debug mode
sql_debug(True)
#
# Map models and create tables if they dont exist
db.generate_mapping(create_tables=True)


###############################################################################

# Get sqlite3 connection
def get_conn(dbname):
    conn = sqlite3.connect(dbname)
    return conn

CHUNK=100000
LIMIT=None

def populateGene2Go(dbname, gene_go):
    conn = get_conn(dbname)
    curs = conn.cursor()
    stream = csv.DictReader(open(gene_go), delimiter='\t')
    stream = islice(stream, LIMIT)
    data = []
    start = time.time()
    for index, row in enumerate(stream):

        data.append((row['GeneID'], row['GO_ID'], row['GO_term'], row['Category']))

        remain = index % CHUNK

        if remain == 0 and data:
            curs.executemany('INSERT INTO Gene2go(geneid, go_id, go_term, category) VALUES (?,?,?,?)', data)
            conn.commit()
            print("commit")
            print(index)

            data = []
    print("Done")

    end = time.time()
    print(end - start)

########################################################################################

def populateGene2Acc(dbname, gene_acc):
    conn = get_conn(dbname)
    curs = conn.cursor()
    stream = csv.DictReader(open(gene_acc), delimiter='\t')
    stream = islice(stream, LIMIT)
    data = []

    start = time.time()

    for index, row in enumerate(stream):

        data.append((row['GeneID'], row['protein_accession.version'], row['Symbol']))

        remain = index % CHUNK

        if remain == 0 and data:
            curs.executemany('INSERT INTO Gene2acc(gene_id, prot_acc, symbol) VALUES (?,?,?)', data)
            conn.commit()
            print("commit")
            print(index)

            data = []
    print("Done")


if __name__ == '__main__':
    populateGene2Go(dbname, gene_go)
    populateGene2Acc(dbname,gene_acc)
