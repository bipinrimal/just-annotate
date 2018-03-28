from query_reflection import *
import csv
from itertools import *

#fname=str(sys.argv[1])
    # query=select(c for c in Gene2go if c.geneid=="814629")
    # for row in query:
    #     print(row.category)

    # query2=select(c for c in Gene2go for d in Protacc if c.geneid==d.gene_id)
    # for row in query2:
    #     print(row.category)


with db_session:
    LIMIT=None
    stream = csv.DictReader(open('blast_testdata'), delimiter='\t')
    stream = islice(stream, LIMIT)
    for index, row in enumerate(stream):
        #print(row["sseqid"])
        # query=select(c for c in Protacc if c.prot_acc==row['sseqid'])
        # for row in query:
        #     print(row.gene_id, row.prot_acc)

        query2=select(g for g in Gene2go for c in Protacc if g.geneid==c.gene_id and c.prot_acc==row['sseqid'])
        # for row in query2:
        #     print(row.geneid, row.go_id, row.go_term, row.category)

        #query3=select(p for p in Protacc if c.prot_acc==row['sseqid'])

        query3=select(( c.prot_acc, g.geneid, g.go_id, g.go_term, g.category)for g in Gene2go for c in Protacc if g.geneid==c.gene_id and c.prot_acc==row['sseqid'])
        for row in query3:
            print(row)
