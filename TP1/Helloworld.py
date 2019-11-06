
import networkx as nx
import matplotlib.pyplot as plt
import FileHandler as fl
import djikstra_algo as algoDji
import Commande as comm
import DijkstraObject as objDij



G = fl.fillGraphFromFile('entrepot.txt')

commandAsked = comm.Command()
commandAsked.setter()

elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]

pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=700)

# edges
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=6)
nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b',style='dashed')

# labels

nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show() # display

#test algo

#TODO: Needs modification here, manque d'independance
length, path = algoDji.graph_to_length(G, 0)
pathToFinalNode = algoDji.path_to_object(G, path, commandAsked)
stops = algoDji.finds_stops(G, pathToFinalNode, commandAsked)


#actionSequence = algoDji.find_way (G, commandAsked)
#print(actionSequence)

print(objDij.fonctionDjikstraObjet(G,commandAsked))