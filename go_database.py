import sqlite3
import os
import csv
from itertools import *


CHUNK=100000
LIMIT=1000000


# A function to create database of name (fname)
def get_conn(fname):
    conn = sqlite3.connect(fname)
    return conn


# A function which creates database (even if database is present,
def create(fname):
    if os.path.isfile(fname):
        os.remove(fname)
    conn = get_conn(fname)
    curs = conn.cursor()

    # create a table
    curs.execute('''CREATE TABLE go_table
               (geneid, protein_acc, symbol)''')

    # Save the table within the database (Save changes)
    conn.commit()


def print_db(fname):
    conn = get_conn(fname)
    curs = conn.cursor()
    print('===')


def play(fname):
    conn = get_conn(fname)
    curs = conn.cursor()

    stream = csv.DictReader(open("gene2accession"), delimiter='\t')
    stream = islice(stream, LIMIT)
    data = []
    for index,row in enumerate(stream):

        data.append((row['GeneID'], row['protein_accession.version'], row['Symbol']))



        remain=index%CHUNK

        if remain==0 and data:
            curs.executemany('INSERT INTO go_table VALUES (?,?,?)', data)
            conn.commit()
            print ("commit")
            print(index)

            data=[]
        # print (row['GeneID'])
    print("Done")


    #print(len(data))
    #1 / 0


    sql_commands=[
        'CREATE INDEX foo1 ON go_table(symbol)',
        'CREATE INDEX foo2 ON go_table(geneid)',
        'CREATE INDEX foo3 ON go_table(protein_acc)',
        ]
    for sql in sql_commands:

        curs.execute(sql)

    print("Index done")
    # search_string=('YP%')
    for row in curs.execute('SELECT COUNT (*) FROM go_table'):
        print(row)

if __name__ == '__main__':
    fname = 'time_db'
    create(fname)
    print_db(fname)
    play(fname)
    print_db(fname)
