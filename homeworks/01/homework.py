# %% Execute entire code
import matplotlib.pyplot as plt
import collections
import random
from networkx import nx

__author__ = 'Gabriel Luciano Gomes - RA 265673'
__email__ = 'g265673@dac.unicamp.br'

def questionOne():   
    """ QUESTION ONE: Create a graph with k = 4 (average degree) """

    N = 10000 # number of nodes
    p = 0.000395 #probability of linking

    G = nx.Graph()
    # building the Graph
    for i in range(N-1):
        G.add_node(i)
        for j in range(i+1,N):
            if random.random() < p:
                G.add_edge(i, j) 

    info = nx.info(G)
    print(info)
      
    plotNormalScale(G, 'normal_scale_01.png')
    plotLogLogScale(G, 'loglog_scale_01.png')
   
def questionTwo():   
    """ QUESTION TWO: Create a graph with k = 4 (average degree) 
    and for every j > 1, add a link (i,j) for node i < j with a
    custom probability p describred bellow.
    """

    N = 10000 # number of nodes
    p = 0.000395 #probability of linking
    e = 0.00001 # épsilon error
  
    # building the Graph
    G = nx.Graph()
    for i in range(N):
        G.add_node(i)

    for i in range(N-1):
        summatory = 0 
        for j in range(i+1,N):            
            summatory += G.degree[j] + e
            if (j > 1):
                customProbability = valueOfP(j, G, G.degree[i], summatory)
                if (random.random() < customProbability): 
                    G.add_edge(i, j) 

    info = nx.info(G)
    print(info)

    plotNormalScale(G, 'normal_scale_02.png')
    plotLogLogScale(G, 'loglog_scale_02.png')

def valueOfP(j, G, kij, summatory):
    """ Calculates the custom probabilty (p) for exercise #2.
    -Parameters:
    j: Execution moment
    G: Graph at J moment
    kij: Degree of node i at moment j
    summatory: accumulative summatory of degrees at moment j    
    """ 
    e = 0.00001 #épsilon error
    q = 4/3 #rational coefficient

    p = ((kij + e)/ summatory) * q
    return p

def plotNormalScale(G, imageName):
    """ Plot and save Normal Scale Graph 
    Parameters:
    -G: Graph to be plotted
    -imageName: name to saved image with its extension (.png)
    """
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color="b")

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg) 

    fig = plt.gcf()
    plt.show()
    fig.savefig(imageName)


def plotLogLogScale(G, imageName):
    """ Plot and save Log Log Scale Graph 

    Parameters:
    -G: Graph to be plotted
    -imageName: name to saved image with its extension (.png)
    """
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    dmax = max(degree_sequence)

    plt.loglog(degree_sequence, "b-", marker="o")
    plt.title("Degree rank plot")
    plt.ylabel("degree")
    plt.xlabel("rank")

    # draw graph in inset
    plt.axes([0.45, 0.45, 0.45, 0.45])
    plt.axis("off")
    fig = plt.gcf()
    plt.show()
    fig.savefig(imageName)

if __name__ == "__main__":
    questionOne()
    questionTwo()


# %%
