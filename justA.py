from itertools import *
import csv
import argparse
from reflection import *


# Parse arguments
parser=argparse.ArgumentParser(description="Query script for obtaining gene ID, go term, category and funciton, "
                                           "and accession number when one is provided")
parser.add_argument("-f","--file",help="File containing either geneID, go term, accession number")
parser.add_argument("-c","--column",help="Column integer value for the data, first=1, second=2")
#parser.add_argument("-t","--type",help="data type:'geneid' if query is geneid; 'protsacc' if query is protein accession number; symbol' if query is gene symbol")
args=parser.parse_args()

fname=str(os.path.abspath(args.file))
col=int(args.column)-1
#data_type=str(args.type)


with db_session:
    LIMIT=10
    stream = csv.DictReader(open(fname), delimiter='\t')
    col_name=stream.fieldnames[col]
    stream = islice(stream, LIMIT)
    for index, row in enumerate(stream):

        query=select(( c.prot_acc, c.symbol, g.geneid, g.go_id, g.go_term, g.category)for g in Gene2go
                     for c in Gene2acc if g.geneid==c.gene_id and c.prot_acc==row[col_name])

        with open('result.csv','wb') as out:
            csv_out = csv.writer(out)
            for row in query:
                print(row)
                csv_out.writerow(row)

# #######################################################################
# with db_session:
#         LIMIT=10
#         stream = csv.DictReader(open(fname), delimiter='\t')
#         col_name=stream.fieldnames[col]
#         stream = islice(stream, LIMIT)
#         for index, row in enumerate(stream):
#
#             query=select((c.symbol, c.prot_acc, g.geneid, g.go_id, g.go_term, g.category)for g in Gene2go
#                          for c in Gene2acc if g.geneid==c.gene_id and c.prot_acc==row[col_name])
#             for row in query:
#                 print(row)
#
#
# ###################################################################################################
#     if data_type=="geneid":
#         LIMIT = 10
#         stream = csv.DictReader(open(fname), delimiter='\t')
#         col_name = stream.fieldnames[col]
#         stream = islice(stream, LIMIT)
#         for index, row in enumerate(stream):
#             query=select(( c.symbol, c.prot_acc, g.geneid, g.go_id, g.go_term, g.category)
#                          for g in Gene2go for c in Gene2acc
#                          if g.geneid==c.gene_id and c.gene_id == row[col_name])
#             for row in query:
#                 print(row)
#
#
# ###################################################################################################
#     if data_type=="symbol":
#         LIMIT = 10
#         stream = csv.DictReader(open(fname), delimiter='\t')
#         col_name = stream.fieldnames[col]
#         stream = islice(stream, LIMIT)
#         for index, row in enumerate(stream):
#
#             query=select(( c.symbol,c.prot_acc, g.geneid, g.go_id, g.go_term, g.category)
#                          for g in Gene2go for c in Gene2acc
#                          if g.geneid==c.gene_id and c.symbol==row[col_name])
#             for row in query:
#                 print(row)