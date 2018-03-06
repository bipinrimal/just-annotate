import sqlite3
import os
import csv
from itertools import *

CHUNK = 10000
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
    curs.execute('''CREATE TABLE gene2go
               (gene_id, go_id, go_term,category)''')

    # Save the table within the database (Save changes)
    conn.commit()


def print_db(fname):
    conn = get_conn(fname)
    curs = conn.cursor()
    print('===')


def play(fname):
    conn = get_conn(fname)
    curs = conn.cursor()

    stream = csv.DictReader(open('gene2go'), delimiter='\t')
    stream = islice(stream, LIMIT)
    data = []
    for index, row in enumerate(stream):

        data.append((row['GeneID'], row['GO_ID'], row['GO_term'], row['Category']))

        remain = index % CHUNK

        if remain == 0 and data:
            curs.executemany('INSERT INTO gene2go VALUES (?,?,?,?)', data)
            conn.commit()
            print("commit")
            print(index)

            data = []
    print("Done")

    sql_commands = [
        'CREATE INDEX gID_index ON gene2go(gene_id)',
        'CREATE INDEX goID_index ON gene2go(go_id)',
        'CREATE INDEX goTERM_index ON gene2go(go_term)',
        'CREATE INDEX category_index ON gene2go(category)',
    ]
    for sql in sql_commands:
        curs.execute(sql)

    print("Index done")

    for row in curs.execute('SELECT COUNT (*) FROM gene2go'):
        print(row)


if __name__ == '__main__':
    fname = "annotationDB"

    create(fname)

    play(fname)
