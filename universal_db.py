import sqlite3
import os
import csv
from itertools import *

CHUNK = 10000
LIMIT = 1000000


# A function to create database of name (fname)
def get_conn(fname):
    conn = sqlite3.connect(fname)
    return conn


# # A function which creates database (even if database is present,
def create(fname, file_name, col_list):
    if os.path.isfile(fname):
        os.remove(fname)
    conn = get_conn(fname)
    curs = conn.cursor()
    # create a table based on the column names given
    create_table_query='CREATE TABLE ' +file_name+str(tuple(col_list))
    curs.execute(create_table_query)
    # Save the table within the database (Save changes)
    conn.commit()


def print_db(fname):
    conn = get_conn(fname)
    curs = conn.cursor()
    print('===')


def play(fname, file_name, col_list):
    conn = get_conn(fname)
    curs = conn.cursor()
    stream = csv.DictReader(open(file_name), delimiter='\t')
    stream = islice(stream, LIMIT)
    data = []

    for index, row in enumerate(stream):

        # data.append((row[str(col_list[0])],row[str(col_list[1])]))
        # data.append((row['GeneID'], row['protein_accession.version'], row['Symbol']))
        # str = "row['GeneID'], row['protein_accession.version'], row['Symbol']"
        tup = ()
        for item in col_list:
            tup = tup + (row[str(item)],)
        print(tup)
        data.append(tup)

        remain = index % CHUNK

        if remain == 0 and data:
            execute_query = "INSERT INTO " + file_name + " VALUES " + '(?,' + '?,' * (len(col_list) - 2) + "?)"
            curs.executemany(execute_query, data)
            conn.commit()
            print("commit")
            print(index)

            data = []
            # print (row['GeneID'])
        print("Done")

    # print(len(data))
    # 1 / 0

    # sql_commands = [
    #     'CREATE INDEX foo1 ON go_table(symbol)',
    #     'CREATE INDEX foo2 ON go_table(geneid)',
    #     'CREATE INDEX foo3 ON go_table(protein_acc)',
    # ]
    # for sql in sql_commands:
    #     curs.execute(sql)

    print("Index done")
    # search_string=('YP%')



if __name__ == '__main__':
    fname = "test_db"
    file_name="gene2acc_light"
    col_list = ['GeneID', 'protein_accession.version', 'Symbol']
    create(fname, file_name, col_list)
    # print_db(fname, )
    play(fname, file_name, col_list)
    # print_db(fname)
