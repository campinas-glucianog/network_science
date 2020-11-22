#%%
import networkx as nx
import pandas as pd
import numpy as np
from Methods import Methods

if __name__ == "__main__":
  data = csv_table=pd.read_table('data/class-network.tsv',sep='\t')
  methods = Methods()
  hobbies = data.columns.values
  hobbies = np.delete(hobbies, 0, 0)
  students = data['class'].tolist()

  # Creating Bipartite Graph
  bipartiteGraph = nx.Graph()
  bipartiteGraph.add_nodes_from(hobbies, bipartite=0)

  bipartiteGraph.add_nodes_from(students, bipartite=1)

  lines = data.to_numpy()
  for line in lines:
    for x in range(1, line.size):
      if(line[x] == 1):
        bipartiteGraph.add_edges_from([(hobbies[x-1], line[0])])
  
  print(nx.info(bipartiteGraph))

  # Executing methods
  methods.plotSetNormalScale(G=bipartiteGraph,
   graphSet=students, imageName="assets/normal_students.png", setName="Students")
  methods.plotSetNormalScale(G=bipartiteGraph,
   graphSet=hobbies, imageName="assets/normal_hobbies.png", setName="Hobbies")
  methods.plotNormalScale(G=bipartiteGraph, imageName="assets/normal_scale.png")

  methods.averageDegree(G=bipartiteGraph, graphSet=students, setName="students")
  methods.averageDegree(G=bipartiteGraph, graphSet=hobbies, setName="hobbies")

  methods.connectedComponents(G=bipartiteGraph)
  methods.averageDistance(G=bipartiteGraph)
  methods.clusteringCoefficient(G=bipartiteGraph)
  methods.createGephiFile(G=bipartiteGraph)

# %%
