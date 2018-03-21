from pony.orm import *


db=Database("sqlite","ponyDB",create_db=True)



class Gene2go(db.Entity):
    """
    Pony ORM Model for Genetogo table containing protein accession link, go-term, go-id and go category
    """

    geneid=Required(str)
    go_term=Required(str)
    go_id=Required(str)
    category=Required(str)
    proteinacc = Set("Protacc")


class Protacc(db.Entity):
    """
    Pony ORM model for Protein accession table containing protein accession, gene symbol and gene_did
    """

    prot_acc=Required(str)
    symbol=Required(str)
    gene_id=Required(Gene2go)


#debug mode
sql_debug(True)
#
# #Map models and create tables if they dont exist
db.generate_mapping(create_tables=True)

###############################################################################

#Insert Data
with db_session:
    g1=Gene2go(geneid="814629",go_term="nucleus",go_id="GO:0005634",category="Component")
    g2=Gene2go(geneid="814629",go_term="biological process",go_id="GO:0008150",category="Process")
    g3=Gene2go(geneid="814630",go_term="DNA binding",go_id="GO:0003677",category="Function")
    g4=Gene2go(geneid="814630",go_term="DNA binding transcription factor activity",go_id="GO:0005634",category="Function")

    p1=Protacc(prot_acc="AAF18653.1",symbol="AT2G01050",gene_id=g1)
    p2=Protacc(prot_acc="AEC05391.1",symbol="AT2G01050",gene_id=g2)

with db_session:
    attr_name="prot_acc"
    param_name="AAF18653.1"
    select(g for g in Gene2go for c in g.proteinacc if getattr(c,attr_name)==param_name)