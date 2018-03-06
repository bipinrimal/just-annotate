import sqlite3
import os
import csv
from itertools import *

CHUNK = 100000
LIMIT = None


# A function to create database of name (fname)
def get_conn(fname):
    conn = sqlite3.connect(fname)
    return conn


def create(fname):
    # if os.path.isfile(fname):
    #     os.remove(fname)
    conn = get_conn(fname)
    curs = conn.cursor()

    # create a table
    curs.execute('''DROP TABLE IF EXISTS gene2acc''')
    curs.execute('''CREATE TABLE gene2acc
               (gene_id, prot_acc, symbol)''')

    # Save the table within the database (Save changes)
    conn.commit()


def print_db(fname):
    conn = get_conn(fname)
    curs = conn.cursor()
    print('===')


def play(fname):
    conn = get_conn(fname)
    curs = conn.cursor()

    stream = csv.DictReader(open('gene2acc'), delimiter='\t')
    stream = islice(stream, LIMIT)
    data = []
    for index, row in enumerate(stream):

        data.append((row['GeneID'], row['protein_accession.version'], row['Symbol']))

        remain = index % CHUNK

        if remain == 0 and data:
            curs.executemany('INSERT INTO gene2acc VALUES (?,?,?)', data)
            conn.commit()
            print("commit")
            print(index)

            data = []
    print("Done")


    sql_commands = [
        'CREATE INDEX symbol_idx ON gene2acc(symbol)',
        'CREATE INDEX gid_idx ON gene2acc(gene_id)',
        'CREATE INDEX pa_idx ON gene2acc(prot_acc)',
    ]
    for sql in sql_commands:
        curs.execute(sql)

    print("Index done")

    for row in curs.execute('SELECT COUNT (*) FROM gene2acc'):
        print(row)


if __name__ == '__main__':
    fname = "annotationDB"
    create(fname)
    play(fname)

