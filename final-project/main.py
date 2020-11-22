
#%%
import pandas as pd

def main():
    dataBase = pd.read_csv("D:/dbs/MO412/steam-200k.csv")

    players = dataBase.user_id
    uniquePlayers = players.unique()
    print(len(uniquePlayers))

    games = dataBase.game_name
    uniqueGames = games.unique()    
    print(len(uniqueGames))

    #Purchased games
    print(dataBase.loc[dataBase['purchase'] == 'purchase'])
    
    #Played Games
    print(dataBase.loc[dataBase['purchase'] == 'play'])




if __name__ == "__main__":
    main()
# %%
