import os
import sys
from pony.orm import *
import sqlite3

db_path=os.path.abspath("annotationDB")
db=Database("sqlite",db_path,create_db=True)

class Gene2go(db.Entity):
    """
    Pony ORM Model for Genetogo table containing protein accession link, go-term, go-id and go category
    """
    geneid = Required(str)
    go_term = Required(str)
    go_id = Required(str)
    category = Required(str)


class Protacc(db.Entity):
    """
    Pony ORM model for Protein accession table containing protein accession, gene symbol and gene_did
    """
    prot_acc = Required(str)
    symbol = Required(str)
    gene_id = Required(str)

# debug mode
#sql_debug(True)

# Map models and create tables if they dont exist
db.generate_mapping(create_tables=True)

