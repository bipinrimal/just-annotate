from pony.orm import *
import os
import sys
import csv
from itertools import *
import time

dbname = str(sys.argv[1])
db = Database("sqlite", dbname, create_db=True)

class Gene2go(db.Entity):
    """
    Pony ORM Model for Genetogo table containing protein accession link, go-term, go-id and go category
    """
    geneid = Required(str,index="gene_id")
    go_term = Required(str)
    go_id = Required(str)
    category = Required(str)


class Protacc(db.Entity):
    """
    Pony ORM model for Protein accession table containing protein accession, gene symbol and gene_id
    """

    prot_acc = Required(str,index="index_protacc")
    symbol = Required(str)
    gene_id = Required(str)

# debug mode
# sql_debug(True)
#
# Map models and create tables if they dont exist
db.generate_mapping(create_tables=True)


###############################################################################

# Insert Data
def populateDB(fname):
    with db_session:
        CHUNK = 100000
        LIMIT = None
        start = time.time()
        stream = csv.DictReader(open(fname), delimiter='\t')
        stream = islice(stream, LIMIT)
        data = []

        for index, row in enumerate(stream):
            data.append(row['GeneID'])
            data.append(row['protein_accession.version'])
            data.append(row['Symbol'])

            Protacc(prot_acc=data[1], symbol=data[2], gene_id=data[0])

            data = []
            remain = index % CHUNK
            if remain == 0:
                print(index)

        print("DONE")
        print("It took %f seconds" % (time.time()-start))


if __name__ == '__main__':
    fname = str(sys.argv[2])
    populateDB(fname)
