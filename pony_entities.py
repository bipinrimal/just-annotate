from pony.orm import *
import os
import sys
import csv
from itertools import *


db=Database("sqlite","annotationDB",create_db=True)


class Genetoacc(db.Entity):
    """
    Pony ORM model for Protein accession table containing protein accession, gene symbol and gene_did
    """

    prot_acc=PrimaryKey(str)
    symbol=Required(str)
    gene_id=Required(str)


class Genetogo(db.Entity):
    """
    Pony ORM Model for Genetogo table containing protein accession link, go-term, go-id and go category
    """

    gene_id=PrimaryKey(str)
    go_term=Required(str)
    go_id=Required(str)
    category=Required(str)



class Blastpresult(db.Entity):
    """
    Pony ORM Model for result table containing protein accession link and stitle
    """

    prot_acc = PrimaryKey(str)
    stitle=Required(str)



#debug mode
sql_debug(True)
#
# #Map models and create tables if they dont exist
db.generate_mapping(create_tables=True)


