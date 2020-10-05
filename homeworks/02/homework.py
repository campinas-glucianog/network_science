# %% Execute entire code
from networkx import nx

__author__ = 'Gabriel Luciano Gomes - RA 265673'
__email__ = 'g265673@dac.unicamp.br'

def questionOne():   
    """ QUESTION ONE: Create a random graph with
    N = 10000 and p = 0.0005 and analyze its properties.
    """
    N = 10000 # number of nodes
    p = 0.0005 #probability of linking

    # building the Graph
    G = nx.gnp_random_graph(N, p)

    # compute de the number of connected componentes
    cc = nx.connected_components(G) #connected components
    ncc = nx.number_connected_components(G) #number of connected components
    print("Number of connected components:", ncc)

    # the size of the giant component
    sortedComponents = sorted(cc, key=len, reverse=True) # sort components in descending order (length)
    gc = G.subgraph(sortedComponents[0]) #the giant component
    print("Size of the giant component:", gc.number_of_nodes())

    # the average distance in the giant component
    ad = nx.average_shortest_path_length(gc)
    print("Average distance in the giant component:", ad)

if __name__ == "__main__":
    questionOne()