from pony.orm import *
import os
import sys
import csv
from itertools import *
import time
import sqlite3

dbname = str(sys.argv[1])
db = Database("sqlite", dbname, create_db=True)

##################################################################################################
class Gene2go(db.Entity):
    """
    Pony ORM Model for Genetogo table containing protein accession link, go-term, go-id and go category
    """
    geneid = Required(str, index="geneid")
    go_term = Required(str, index="go_term")
    go_id = Required(str, index="go_id")
    category = Required(str, index="category")

class Protacc(db.Entity):
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

def play(dbname, fname):
    conn = get_conn(dbname)
    curs = conn.cursor()
    stream = csv.DictReader(open(fname), delimiter='\t')
    stream = islice(stream, LIMIT)
    data = []

    start = time.time()

    for index, row in enumerate(stream):

        data.append((row['GeneID'], row['protein_accession.version'], row['Symbol']))

        remain = index % CHUNK

        if remain == 0 and data:
            curs.executemany('INSERT INTO Protacc (gene_id, prot_acc, symbol) VALUES (?,?,?)', data)
            conn.commit()
            print("commit")
            print(index)

            data = []
    print("Done")

    end = time.time()
    print(end - start)

if __name__ == '__main__':
    dbname = str(sys.argv[1])
    fname = str(sys.argv[2])
    play(dbname, fname)

