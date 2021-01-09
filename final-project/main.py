#%%
import pandas as pd
import networkx as nwx
from algorithms import Algorithms

__author__ = 'Gabriel Luciano Gomes - RA 265673, Paulo Junio Reis Rodrigues RA - 265674'
__email__ = '{g265673, p265674}@dac.unicamp.br'

algorithms = Algorithms()

def executeMethods(G, fileName, db):
    # Degree Distribution 
    # algorithms.averageDistance(G)
    algorithms.connectedComponents(G)
    largest_cc = algorithms.retrieveLargestComponent(G)
    # algorithms.plotNormalScale(G,
    #     "User Degree Distribution", "user_distribution.png", db.user_id.unique())

    # algorithms.plotNormalScale(G,
    #     "Game Degree Distribution", "game_distribution.png", db.game_name.unique())
    
    # algorithms.clusteringCoefficient(G)
    # algorithms.plotLoglogScale(largest_cc, fileName)
    # algorithms.degreeCorrelationMatrix(largest_cc)
    # algorithms.clusteringCoefficient(largest_cc)
    algorithms.assortativityCoefficient(largest_cc)
    # algorithms.randomFailures(largest_cc, 0.05)
    # algorithms.drawNetwork(largest_cc)
    # algorithms.plotCommunities(largest_cc)


def main():
    dataBase = pd.read_csv("D:/dbs/MO412/steam-200k.csv")  
    algorithms.verifyDatabaseInfo(dataBase)

    #Purchased games database
    purchased_db = dataBase.loc[dataBase['purchase'] == 'purchase'] 
    #Purchased games network
    G_purchased = nwx.from_pandas_edgelist(
        df=purchased_db,
        create_using=nwx.Graph(),
        source='user_id',
        target='game_name')
    

    #Played Games database
    #played_db = dataBase.loc[dataBase['purchase'] == 'play']
    #Played games network
    #G_played = nwx.from_pandas_edgelist(played_db, 'user_id', 'game_name', ['hours_played'])


    executeMethods(G_purchased, 'purchased_graph.png', db = purchased_db)

if __name__ == "__main__":
    main()
# %%
