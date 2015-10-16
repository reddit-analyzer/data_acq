import networkx as nx
from itertools import cycle
import matplotlib.pyplot as plt
import csv
import os
import re

os.chdir("/Users/htom/Desktop/Backup/MSAN_Fall_2015/Data_Acq/Reddit_project/Analysis/")

# Stop word list
stopwords = \
    ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also',
     'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be',
     'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear',
     'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for',
     'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers',
     'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is',
     'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may',
     'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor',
     'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our',
     'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since',
     'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then',
     'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us',
     've', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which',
     'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet',
     'you', 'your']



G = nx.Graph()

#generate edge list of cleaned words
with open('comments4graph.csv', 'rb') as f:
    reader = csv.reader(f)
    sentence_list = list(reader)

giant_list = []
for item in sentence_list:
    line = re.sub('[^\w\s]', '', str(item).lower())
    line = line.encode('ascii','ignore')
    giant_list.append(line.split())


giant_wordlist = [value for sublist in giant_list for value in sublist]
giant_wordlist = [item for item in giant_wordlist if item not in stopwords]
edge_list = giant_wordlist[0:100]
edge_cycle = cycle(edge_list)
nextitem = edge_cycle.next()
i = 1
while i < len(edge_list):
    cur_item, nextitem = nextitem, edge_cycle.next()
    edge = (cur_item, nextitem)
    G.add_edge(*edge)
    # print cur_item, nextitem
    i += 1

# pos = nx.graphviz_layout(G)
nx.draw_circular(G, node_size = 5)
plt.show()

myfile = open("testoutfile.csv", 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
for word in giant_wordlist:
    wr.writerow([word])

# giant_uniqword = set(giant_wordlist)

# print giant_wordlist[0:100]

# print sentence_list[0]
# test = sentence_list[0]
# # line = re.sub('[!@#$\[\]"\'.]', '', str(test))
# line = re.sub('[^\w\s]', '', str(test))
#
# print sentence_list[1]