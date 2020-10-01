# %% Execute entire code
import matplotlib.pyplot as plt
import collections
import random
import timeit
from networkx import nx

__author__ = 'Gabriel Luciano Gomes - RA 265673'
__email__ = 'g265673@dac.unicamp.br'

def questionOne():   
    """ QUESTION ONE: Create a graph with k = 4 (average degree) """

    N = 10000 # number of nodes
    p = 0.000398 #probability of linking

    # building the Graph
    G = nx.Graph()
    for i in range(N):
        G.add_node(i)

    for i in range(N):
        for j in range(i+1,N):
            if random.random() < p:
                G.add_edge(i, j) 

    info = nx.info(G)
    print(info)
      
    plotNormalScale(G, 'normal_scale_01.png')
    plotLogLogScale(G, 'loglog_scale_01.png')
   
def questionTwo():   
    """ QUESTION TWO: Create a graph with the following property:
    for every j > 1, add a link (i,j) for node i < j with a
    custom probability p describred bellow.
    p = ((kij + e)/sum_{m=1}^{j-1}(k_{mj}+e))*q
    where: 
        - kij = Degree of node i at moment j
        - e = épsilon error 
        - q = rational coefficient
    """

    start = timeit.default_timer()

    N = 10000 # number of nodes
    e = 0.00001 # épsilon error
  
    # building the Graph
    G = nx.Graph()
    for i in range(N):
        G.add_node(i)

    for j in range(N):
        summatory = 0
        for m in range(1, j):
            summatory += G.degree[m] + e 

        for i in range(1, j):
            if (j > 1):
                customProbability = valueOfP(G.degree[i], summatory)
                if (random.random() < customProbability): 
                    G.add_edge(i, j) 

    info = nx.info(G)
    print(info)

    plotNormalScale(G, 'normal_scale_02.png')
    plotLogLogScale(G, 'loglog_scale_02.png')

    stop = timeit.default_timer()
    print('Time: ', stop - start) 

def valueOfP(kij, summatory):
    """ Calculates the custom probabilty (p) for exercise #2.
    -Parameters:
    kij: Degree of node i at moment j
    summatory: sum of degress at moment j
    """ 
    e = 0.00001 #épsilon error
    q = 4/3 #rational coefficient

    p = ((kij + e)/summatory) * q
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
    #questionOne()
    questionTwo()


# %%
