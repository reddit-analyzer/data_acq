import networkx as nx
from itertools import cycle
import matplotlib.pyplot as plt
import csv
import os
import re

os.chdir("/Users/htom/Desktop/Backup/MSAN_Fall_2015/Data_Acq/Reddit_project/Analysis/")

G = nx.Graph()

#generate edge list of cleaned words
with open('domain4graph.csv', 'rb') as f:
    reader = csv.reader(f)
    pairs = list(reader)

giant_listoflists = [item for item in pairs]

giant_list = [value for sublist in giant_listoflists for value in sublist]
giant_uniq = list(set(giant_list))
edge_list = giant_list
edge_cycle = cycle(edge_list)
nextitem = edge_cycle.next()
i = 1
while i < len(edge_list):
    cur_item, nextitem = nextitem, edge_cycle.next()
    edge = (cur_item, nextitem)
    G.add_edge(*edge)
    # print cur_item, nextitem
    i += 1

hubs = ["aww","nottheonion","television","AnimalsBeingJerks","worldnews"]
labels1 = {}
for node in G.nodes():
    if node in hubs:
        #set the node name as the key and the label as its value
        labels1[node] = node
print labels1

colors = range(G.number_of_edges())
nx.draw(G, node_size = 5, with_labels=True, labels = labels1,
        font_size = 16, font_color = 'r', font_family = "serif",
        node_color = 'b', edge_color = colors, edge_cmap=plt.cm.Blues)

plt.savefig('subredditPlot.pdf')
# plt.show()
