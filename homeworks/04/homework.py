# %%
from networkx import nx
import matplotlib.pyplot as plt
import collections
import numpy as np

__author__ = 'Gabriel Luciano Gomes - RA 265673'
__email__ = 'g265673@dac.unicamp.br'

def buildGraph(filePath): 
    G = nx.DiGraph()
    file = open(filePath, "r")
    for line in file:
        x, y = line.rstrip("\n").split('\t')
        G.add_edge(x, y)
    return G       

def plotLoglogScale(data, imageName):
    """ Plot and save Log Log Scale Graph 
    Parameters:
    -data: data to be plotted
    -imageName: name to saved image with its extension (.png)
    """
    nodes, nodes_degree  = [n for n, d in data], [d for n, d in data]
    degreeCount = collections.Counter(nodes_degree) 
    accDegree = sorted(degreeCount.items(), key=lambda pair: pair[0], reverse=False) 
    
    degreeSeq = np.zeros(int(max(nodes_degree))+1)

    for x, y in accDegree:
        degreeSeq[x] = y

    degreeSeq = degreeSeq/int(max(nodes))
    plt.loglog(degreeSeq, "b-", marker="o")
    plt.title("Degree rank plot")
    plt.ylabel("Probability of degree")
    plt.xlabel("Degree")

    # draw graph in inset
    plt.axes([0.45, 0.45, 0.45, 0.45])
    plt.axis("off")
    fig = plt.gcf()
    plt.show()
    fig.savefig(imageName)



if __name__ == "__main__":
    graph = buildGraph("net.txt")
    # plotLoglogScale(graph.out_degree, "outgoing_degree_distribution.png")
    plotLoglogScale(graph.in_degree, "incoming_degree_distribution.png")
