# %% Generate Value of p
import matplotlib.pyplot as plt
import collections
import random
from networkx import nx

""" QUESTION ONE """
def questionOne():   

    N = 10000 # number of nodes
    p = 0.000395 #probability of :inking

    G = nx.Graph()
    # building the Graph
    for i in range(N-1):
        G.add_node(i)
        for j in range(i+1,N):
            if random.random() < p:
                G.add_edge(i, j); 

    info = nx.info(G)
    print(info)
      
    plotNormalScale(G)
    plotLogLogScale(G)
   

def plotNormalScale(G):
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

    plt.savefig("degree_normal_scale.png") 


def plotLogLogScale(G):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    dmax = max(degree_sequence)

    plt.loglog(degree_sequence, "b-", marker="o")
    plt.title("Degree rank plot")
    plt.ylabel("degree")
    plt.xlabel("rank")

    # draw graph in inset
    plt.axes([0.45, 0.45, 0.45, 0.45])
    plt.axis("off")
    plt.show()
    plt.savefig("degree_log_log_scale.png")  


def valueOfP(j, G, kij):
    summatory = 0
    for index, degree in G.degree:
        if(index != j):
            continue


if __name__ == "__main__":
    questionOne()




# %%
