DATA_DIR=data/ncbi
DB_DIR=data/db

DATA_TEST_DIR=data/test

all:
    query

data/ncbi:
	mkdir -p data/ncbi

data/db:
	mkdir -p data/db


dir: data/ncbi

db: data/db

data: dir
	(cd ${DATA_DIR} && curl ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2go.gz >gene2go.gz )
	gunzip ${DATA_DIR}/gene2go.gz
	(cd ${DATA_DIR} && curl ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2accession.gz >gene2accession.gz)
	gunzip ${DATA_DIR}/gene2accession.gz


build: data db
	python gene2go(pony).py ${DB_DIR}/annotationDB ${DATA_DIR}/gene2go
    python gene2acc(pony).py ${DB_DIR}/annotationDB ${DATA_DIR}/gene2accession

query:
    python pony_queries.py ${DB_DIR}/annotationDB



