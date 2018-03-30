# just-Annotate
Functional analysis of genomic data 

**Just annotate** is a tool for genome annotation which uses sqlite based database created from NCBI GeneID to 
Gene Ontology mapping file and Gene ID to protein accession numbers mapping file and queries the database using 
Pony ORM library. It takes protein accession number obtained from blast result as input and annotates it 
with gene symbol, gene ontology term, gene ontology id and the category.  

  
    
    
**Usage:**
     
    python justA.py  
     
    justA.py [-h] [-f FILE] [-c COLUMN]
     
    Query script for obtaining gene ID, go term, category and funciton, when
    accession number is provided.
      
    optional arguments:  
     
    -h, --help            show this help message and exit
    
    -f FILE, --file FILE  
                        File containing either geneID, go term, accession number
                         
    -c COLUMN, --column COLUMN
                        Integer value for the column containing query data, first column=1, second column =2




**Install Dependencies:**

Pony ORM
```bash
    pip install pony
```

**Install:**

```bash
git clone https://github.com/bipinrimal/just-annotate.git
cd just-annotate
make
```
The installation involves building a sqlite based database compatible with Pony ORM query library.
It takes about 4-5 minutes for the data file to download based on the internet connection and building the database
requires about 40-45 minutes.

The tables within the built database ncludes:

**A. Gene2go:** 
1. *geneid* (Gene ID)
2. *go_id* (Gene Ontology ID)
3. *go_term* (Gene Ontology Term)
4. *category* (Category)


**B. Gene2acc:** 
1. *gene_id* (Gene ID)
2. *prot_acc* (Protein Accession no.)
3. *symbol*    (Gene Symbol)


**Usage Example:**

The *justA.py* can take blast output table as input with the column number containing the query Protein accession
 number. 
 
 ```bash
$ python justA.py -f blast_testdata.txt -c 2
  
(u'AAA17565.1', u'MYO1C', u'281937', u'GO:0001726', u'ruffle', u'Component')
(u'AAA17565.1', u'MYO1C', u'281937', u'GO:0003777', u'microtubule motor activity', u'Function')
(u'AAA17565.1', u'MYO1C', u'281937', u'GO:0003779', u'actin binding', u'Function')
(u'AAA17565.1', u'MYO1C', u'281937', u'GO:0005102', u'signaling receptor binding', u'Function')
(u'AAA17565.1', u'MYO1C', u'281937', u'GO:0005516', u'calmodulin binding', u'Function')
(u'AAA17565.1', u'MYO1C', u'281937', u'GO:0005524', u'ATP binding', u'Function')
(u'AAA17565.1', u'MYO1C', u'281937', u'GO:0005643', u'nuclear pore', u'Component')
(u'AAA17565.1', u'MYO1C', u'281937', u'GO:0005730', u'nucleolus', u'Component')
(u'AAA17565.1', u'MYO1C', u'281937', u'GO:0005902', u'microvillus', u'Component')

```