# just-annotate
Functional analysis of genomic data 

There are three scripts *gene2go.py*, *gene2acc.py* and *results.py* which create sqlite3 databases for NCBI
GeneID to Gene Ontology mapping file, Gene ID to protein accession numbers mapping file and finally the user Diamond result file containing protein accession number and sequence title.
 
*gene2go.py* creates the annotation database so need to be run first. Others can be run after that. 

The tables includes:

**A. gene2go:** (Created by *gene2go.py*)
1. *gene_id* (Gene ID)
2. *go_id* (Gene Ontology ID)
3. *go_term* (Gene Ontology Term)
4. *category* (Category)


**B. gene2acc:** (Created by *gene2acc.py*)
1. *gene_id* (Gene ID)
2. *prot_acc* (Protein Accession no.)
3. *symbol*    (Gene Symbol)

**C. blastresult:** (Created by *results.py*)
1. *prot_acc* (Protein Accession no.)
2. *stitle* (Sequence Title from Blastp result)

