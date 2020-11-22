import collections
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms import bipartite

class Methods: 

  def plotSetNormalScale(self, G, graphSet, imageName, setName):    
    distribution = []
    for edge in graphSet:
      distribution.append([edge, len(G.edges(edge))])
    
    plt.bar([s for s, d in distribution], [d for s, d in distribution])
    fig = plt.gcf()
    plt.title("{0} Degree Histogram".format(setName))
    plt.ylabel("Hobbies" if setName == "Students" else "Students")
    plt.xlabel(setName)
    plt.show()
    fig.savefig(imageName)  

  def plotNormalScale(self, G, imageName):
    """ Plot and save Normal Scale Graph 
    Parameters:
    -G: Graph to be plotted
    -imageName: name to saved image with its extension (.png)
    """
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80)

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg) 

    fig = plt.gcf()
    plt.show()
    fig.savefig(imageName)   

  def plotLoglogScale(self, G, imageName):
    """ Plot and save Log Log Scale Graph 
    Parameters:
    -G: graph to be plotted
    -imageName: name to saved image with its extension (.png)
    """
    data = G.degree()
    nodes, nodes_degree  = [n for n, d in data], [d for n, d in data]
    degreeCount = collections.Counter(nodes_degree) 
    accDegree = sorted(degreeCount.items(), key=lambda pair: pair[0], reverse=False) 
    
    degreeSeq = np.zeros(int(max(nodes_degree))+1)

    print("Degree distribution: ", degreeCount)

    for x, y in accDegree:
      degreeSeq[x] = y

    degreeSeq = degreeSeq/int(len(nodes))
    plt.loglog(degreeSeq, marker="o")
    plt.title("Degree rank plot")
    plt.ylabel("Probability of degree")
    plt.xlabel("Degree")

    # draw graph in inset
    plt.axes([0.45, 0.45, 0.45, 0.45])
    plt.axis("off")
    fig = plt.gcf()
    plt.show()
    fig.savefig(imageName)


  def averageDegree(self, G, graphSet, setName):
    numEdges = G.number_of_edges()
    average_degree = numEdges/len(graphSet) 

    print("Average degree for {0} set: {1}".format(setName, average_degree))

  def connectedComponents(self, G):
    """ Compute the number of connected components 
    and size of the giant component
    Parameters:
    -G: graph to be analysed
    """    
    cc = nx.connected_components(G)
    ncc = nx.number_connected_components(G)
    print("Number of connected components:", ncc)

     # the size of the giant component
    sortedComponents = sorted(cc, key=len, reverse=True) # sort components in descending order (length)
    gc = G.subgraph(sortedComponents[0]) #the giant component
    print("Size of the giant component:", gc.number_of_nodes())

  def averageDistance(self, G):
    """ Compute graph average distance
    Parameters:
    G- graph to be analysed
    """
    ad = nx.average_shortest_path_length(G)
    print("Average distance within the graph:", ad)

  def clusteringCoefficient(self, G):
    """ Compute graph clustering coefficient
    Parameters:
    G- graph to be analysed
    """
    hobbies, students = bipartite.sets(G)
    wholeCC = bipartite.average_clustering(G)
    hobbiesCC = bipartite.average_clustering(G, hobbies)
    studentsCC = bipartite.average_clustering(G, students)
    print("Whole Graph Average clustering coef:", wholeCC)
    print("Hobbies Set Average clustering coef:", hobbiesCC)
    print("Students set Average clustering coef", studentsCC)


  def createGephiFile(self, G):
    """ Create file to be read in Gephi
    Parameters:
    G- graph to be written in the file
    """
    f = open("data/network_for_gephi.csv", "a")
    for s, d in G.edges():
      f.writelines("{0},{1}\n".format(s, d))

    f.close()





