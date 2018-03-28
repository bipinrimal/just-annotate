# just-annotate
Functional analysis of genomic data 

There are three scripts *gene2go.py*, *gene2acc.py* and *results.py* which create a sqlite3 database for NCBI
GeneID to Gene Ontology mapping file, Gene ID to protein accession numbers mapping file and finally the user Diamond 
result file containing protein accession number and sequence title.
 
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

The database can be queried to identify gene symbol and gene ontology terms for the protein accession obtained from blastp result. 
For example:

    Input Query:
    curs.execute('''SELECT blastresult.prot_acc, gene2acc.gene_id, gene2acc.symbol, gene2go.go_id, gene2go.gene_id, gene2go.go_term
        FROM blastresult JOIN gene2go JOIN gene2acc
        ON blastresult.prot_acc = gene2acc.prot_acc AND gene2acc.gene_id = gene2go.gene_id LIMIT 10;''')
        
     
    Output: 
    NP_181643.1,818709,TCH3,GO:0005509,818709,"calcium ion binding"
    NP_181643.1,818709,TCH3,GO:0005509,818709,"calcium ion binding"
    NP_181643.1,818709,TCH3,GO:0005509,818709,"calcium ion binding"
    NP_181643.1,818709,TCH3,GO:0005509,818709,"calcium ion binding"
    NP_181643.1,818709,TCH3,GO:0005509,818709,"calcium ion binding"
    NP_181643.1,818709,TCH3,GO:0005509,818709,"calcium ion binding"
    NP_181643.1,818709,TCH3,GO:0005509,818709,"calcium ion binding"
    NP_181643.1,818709,TCH3,GO:0005509,818709,"calcium ion binding"
    NP_181643.1,818709,TCH3,GO:0005515,818709,"protein binding"
    NP_181643.1,818709,TCH3,GO:0005515,818709,"protein binding"
           