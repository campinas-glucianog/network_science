#!/usr/bin/python3
# %%
import networkx as nx
import matplotlib.pyplot as plt
from numpy import arange
import random

__author__ = 'Gabriel Luciano Gomes - RA 265673'
__email__ = 'g265673@dac.unicamp.br'

def buildGraph(filepath):
  networkFile = open(filepath, 'r')
  G = nx.Graph()

  for line in networkFile.readlines():
    x, y = line.split()
    G.add_edge(x.strip(), y.strip())
  return G

def randomFailures(G, increments):
   """ 
    Computes and plots the network robustness against random failures.
    To do so, calculate the relative size of the giant component after
    an f fraction of routes randomly removed 
      :param G: Graph to be analysed
      :param increments: f fraction of nodes to be removed
      :type G: Networkx graph
      :type increments: int
    """
  # calculate the relative size of the giant component
  # after an f fraction of routers are randomly removed.
  graph_copy = nx.Graph(G)
  n_nodes = graph_copy.number_of_nodes()
  remove_percent = int(increments * graph_copy.number_of_nodes())
  p_inf = []

  p_inf.append(
    len(max(nx.connected_components(graph_copy), key=len)) / n_nodes
  )

  for i, f in enumerate(arange(0.05, 1.0, 0.05)):
    current_nodes = list(graph_copy.nodes())
    nodes_to_remove = random.sample(current_nodes, remove_percent)
    graph_copy.remove_nodes_from(nodes_to_remove)
    p_inf.append(
      len(max(nx.connected_components(graph_copy), key=len))
       / 
        (n_nodes - ((i+1)*remove_percent)) # Normalization [0, 1]
    )

  plt.plot([f for f in arange(0, 1.0, 0.05)], [p_inf[f]/p_inf[0] for f in range(20)])
  plt.ylabel('P$\infty$( f ) / P $\infty$(0)')
  plt.xlabel('f', fontsize=15)
  fig = plt.gcf()
  plt.show()
  fig.savefig('p_inf[f]_p_inf[0].png')

if __name__ == "__main__":
  graph = buildGraph('netA.txt')
  randomFailures(graph, 0.05)

# %%
