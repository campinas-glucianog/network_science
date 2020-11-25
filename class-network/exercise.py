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
    
  hobbiesProjection, studentProjection = methods.createProjections(bipartiteGraph)

  # Executing methods for whole graph
  methods.plotSetNormalScale(G=bipartiteGraph,
   graphSet=students, imageName="assets/normal_students.png", setName="Students")
  methods.plotSetNormalScale(G=bipartiteGraph,
   graphSet=hobbies, imageName="assets/normal_hobbies.png", setName="Hobbies")

  methods.plotNormalScale(G=bipartiteGraph, 
    plotTitle="Bipartite Graph Degree Histogram", 
    imageName="assets/normal_scale.png")
  methods.averageDegree(G=bipartiteGraph, graphSet=students, setName="students")
  methods.averageDegree(G=bipartiteGraph, graphSet=hobbies, setName="hobbies")

  methods.connectedComponents(G=bipartiteGraph)
  methods.averageDistance(G=bipartiteGraph)
  methods.clusteringCoefficient(G=bipartiteGraph)
  methods.createGephiFile(G=bipartiteGraph, fileName = "whole_graph")


  #Methods for hobbies Projection
  print(nx.info(hobbiesProjection))
  methods.plotNormalScale(G=hobbiesProjection, 
    plotTitle="Hobbies Projection Degree Histogram", 
    imageName="assets/hobbies_normal_scale.png")
  methods.connectedComponents(G=hobbiesProjection)
  methods.averageDistance(G=hobbiesProjection)
  methods.clusteringCoefficient(G=hobbiesProjection)
  methods.clusteringCoefficientSingle(G=hobbiesProjection, nodes = hobbies)
  methods.createGephiFile(G=hobbiesProjection, fileName = "hobbies_projection")

  #Methods for student projection
  print(nx.info(studentProjection))
  methods.plotNormalScale(G=hobbiesProjection, 
    plotTitle="Students Projection Degree Histogram", 
    imageName="assets/students_normal_scale.png")
  methods.connectedComponents(G=studentProjection)
  methods.averageDistance(G=studentProjection)
  methods.clusteringCoefficient(G=studentProjection)
  methods.clusteringCoefficientSingle(G=studentProjection, nodes = students )
  methods.createGephiFile(G=studentProjection, fileName = "students_projection")


# %%
