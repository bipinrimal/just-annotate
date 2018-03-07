DATA_DIR=data/ncbi
DB_DIR=data/db

DATA_TEST_DIR=data/test

data/ncbi:
	mkdir -p data/ncbi

data/test:
	mkdir -p data/test

data/db:
	mkdir -p data/db



dir: data/ncbi

test_dir: data/test



db: data/db

data: dir
	(cd ${DATA_DIR} && curl ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2go.gz >gene2go.gz )
	gunzip ${DATA_DIR}/gene2go.gz
	#(cd ${DATA_DIR} && curl ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2accession.gz >gene2accession.gz)
	#gunzip ${DATA_DIR}/gene2accession.gz

build: data db
	python gene2go.py ${DB_DIR}/annotationDB ${DATA_DIR}/gene2go
    	#python gene2acc.py ${DATA_DIR}/gene2accession




build_test: test_dir dir db
	python gene2go.py ${DATA_TEST_DIR}/testDB ${DATA_DIR}/gene2go
	python gene2acc.py ${DATA_TEST_DIR}/testDB ${DATA_TEST_DIR}/gene2acc_light
	python results.py ${DATA_TEST_DIR}/testDB ${DATA_TEST_DIR}/blast_testdata



