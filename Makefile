
DATA_HOST=data.bioinformatics.recipes

# The initial data for all recipes
DATA_FILE=recipes-initial-data.tar.gz
TEST_DIR=export/local/test_dir
MAP_DIR=export/local/map_dir

all:
	make test
	#make id

#Create Directories for the files
test_dir: .
	mkdir -p ${TEST_DIR}
#map_dir:.
	#mkdir -p ${MAP_DIR}

#Download test data
test: test_dir
	(cd ${TEST_DIR} && curl http://${DATA_HOST} > ${DATA_FILE} )
	(cd ${TEST_DIR} && tar zxvf ${DATA_FILE})

#Download id mapping file from uniprot
#id: map_dir
	#(cd ${MAP_DIR} && curl http://${DATA_HOST}/initial/${DATA_FILE} > ${DATA_FILE} )
	#(cd ${MAP_DIR} && tar zxvf ${DATA_FILE})