# %%
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def degreeCorrelationMatrix(G):
  avg_degree = sum(int(a_tuple[1]) for a_tuple in G.degree())/int(G.number_of_nodes())

  degrees = [y for x,y in G.degree()]
  degrees_set = list(set(degrees))

  graph_edges = G.edges()

  pis = [0 for i in range(max(degrees_set)+1)]
  qis = [0 for i in range(max(degrees_set)+1)]
  correlation_matrix = [[0 for i in range(max(degrees_set)+1)] for j in range(max(degrees_set)+1)]

  # compute probabilities of degrees
  for degree in degrees_set:
    pis[int(degree)] = degrees.count(degree)/G.number_of_nodes()

  # compute q_k values
  for degree in degrees_set:
    node_count = degrees.count(degree)
    q_k = (degree * pis[int(degree)]) / avg_degree
    qis[int(degree)] = q_k

  for i in range(1, max(degrees_set)):
    for j in range(i+1, max(degrees_set)+1):

      fraction_qi = 1
      
      if degrees.count(i) != 0:
        fraction_qi = qis[i+1] / degrees.count(i)

      link_counter = 0
      for (node_i, node_j) in G.edges:
        if G.degree(node_i) == i and G.degree(node_j) == j:
          link_counter += 1
        elif G.degree(node_i) == j and G.degree(node_j) == i:
          link_counter += 1
      correlation_matrix[i][j] = link_counter * fraction_qi
      correlation_matrix[j][i] = link_counter * fraction_qi

  sns_plot = sns.heatmap(correlation_matrix, cmap="YlGnBu")
  figure = sns_plot.get_figure()    
  figure.savefig('svm_conf.png', dpi=400)
  print("DONE")

def plotDegreeCorrelationFunction(G):
  degreeCorrelation = nx.average_degree_connectivity(G)
  dc_sorted = dict(sorted(degreeCorrelation.items()))
  plt.title('Degree Correlation Function')
  plt.ylabel('Knn(K)')
  plt.xlabel('K')
  plt.loglog(list(dc_sorted.keys()), list(dc_sorted.values()), '.')
  plt.show()

def degreeCorrelationCoefficient(G):
  print("Degree correlation coefficient:{0}"
    .format(nx.degree_pearson_correlation_coefficient(G)))

if __name__ == "__main__":
  networkFile = open('net8.txt', 'r')
  G = nx.Graph()

  for line in networkFile.readlines():
    x, y = line.split()
    G.add_edge(x, y)
  
    
  # Degree Correlation Matrix
  degreeCorrelationMatrix(G)

  # Degree Correlation  
  plotDegreeCorrelationFunction(G)    

  # Degree Correlation Coefficient
  degreeCorrelationCoefficient(G)
  
# %%
