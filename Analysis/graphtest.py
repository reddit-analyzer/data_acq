import networkx as nx
from itertools import cycle
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node("a")
G.add_nodes_from(["b","c"])

G.add_edge(1,2)
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)
G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])


nx.draw_networkx(G)
plt.show()

################################################################
from itertools import cycle

G = nx.Graph()
# edge_list = ["the","cat","ate","the","hat","the","cat","ate","money"]
edge_list = ["cat","ate","hat","cat","ate","money"]
edge_cycle = cycle(edge_list)
nextitem = edge_cycle.next()
i = 1
while i < len(edge_list):
    cur_item, nextitem = nextitem, edge_cycle.next()
    edge = (cur_item, nextitem)
    G.add_edge(*edge)
    # print cur_item, nextitem
    i += 1

G.add_edge(*edge)

nx.draw_networkx(G)
plt.show()