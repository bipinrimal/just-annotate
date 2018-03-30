DATA_DIR=data/ncbi
DB_DIR=data/db

all:dir data build

dir:
	mkdir -p ${DATA_DIR}
	mkdir -p ${DB_DIR}

data: dir
	(cd ${DATA_DIR} && curl ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2go.gz >gene2go.gz )
	gunzip ${DATA_DIR}/gene2go.gz
	(cd ${DATA_DIR} && curl ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2accession.gz >gene2accession.gz)
	gunzip ${DATA_DIR}/gene2accession.gz


build: data
	python build.py -db ${DB_DIR}/annotationDB -g ${DATA_DIR}/gene2go -p ${DATA_DIR}/gene2accession




