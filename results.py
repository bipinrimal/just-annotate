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
    curs.execute('''DROP TABLE IF EXISTS blastresult''')
    curs.execute('''CREATE TABLE blastresult
               (prot_acc,stitle)''')

    # Save the table within the database (Save changes)
    conn.commit()


def print_db(fname):
    conn = get_conn(fname)
    curs = conn.cursor()
    print('===')


def play(fname):
    conn = get_conn(fname)
    curs = conn.cursor()
    stream = csv.DictReader(open('blastpresult'), delimiter='\t')
    stream = islice(stream, LIMIT)
    data = []
    for index, row in enumerate(stream):

        data.append((row['sseqid'], row['stitle']))

        remain = index % CHUNK

        if remain == 0 and data:
            curs.executemany('INSERT INTO blastresult VALUES (?,?)', data)
            conn.commit()
            print("commit")
            print(index)

            data = []
    print("Done")

    sql_commands = [
        'CREATE INDEX protacc_idx ON blastresult(prot_acc)',
        'CREATE INDEX stitle_idx ON blastresult(stitle)',
    ]
    for sql in sql_commands:
        curs.execute(sql)

    print("Index done")

    for row in curs.execute('SELECT COUNT (*) FROM blastresult'):
        print(row)

    curs.execute('''SELECT blastresult.prot_acc, gene2acc.gene_id, gene2acc.symbol, gene2go.go_id, gene2go.gene_id, gene2go.go_term
        FROM blastresult JOIN gene2go JOIN gene2acc
        ON blastresult.prot_acc = gene2acc.prot_acc AND gene2acc.gene_id = gene2go.gene_id LIMIT 10;''')

if __name__ == '__main__':
    fname = "annotationDB"
    create(fname)
    play(fname)
