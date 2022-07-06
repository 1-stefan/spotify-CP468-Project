import pandas as pd 

df60s = pd.read_csv("dataset-of-60s.csv")
df70s = pd.read_csv("dataset-of-70s.csv")
df80s = pd.read_csv("dataset-of-80s.csv")
df90s = pd.read_csv("dataset-of-90s.csv")
df00s = pd.read_csv("dataset-of-00s.csv")
df10s = pd.read_csv("dataset-of-10s.csv")

#print(df60s)

#print(df60s.columns)

#target is whether the song is a hit or not 1 = hit song, 0 = not a hit

#this is the full df
#df = pd.concat(map(pd.read_csv, ["dataset-of-60s.csv", "dataset-of-70s.csv", "dataset-of-80s.csv", "dataset-of-90s.csv", "dataset-of-00s.csv", "dataset-of-10s.csv"]), ignore_index = True)
#df.dropna()

##print(df)

#print(df.iloc[-1:])

#print(df.tail())

#checking if df is properly filled ^^

#print(df.info())

dfs = [pd.read_csv(f"dataset-of-{decade}0s.csv") for decade in ['6','7','8','9','0','1']]
print(dfs[1])
for i, decade in enumerate([1960,1970,1980,1990,2000,2010]):
    dfs[i]['decade'] = pd.Series(decade, index = dfs[i].index)

print(dfs[5])



#shuffle our complete df of all decades so that they are not in order

df = pd.concat(dfs, axis = 0).sample(frac = 1.0, random_state = 1).reset_index(drop = True)
print(df)

#check na and drop object because not relevant

print(df.info())

#make a copy for editing and preprocessing
def preprocess(df):
    dfCopy = df.copy()

    #we want to drop categorical values that have nothing to do with our analysis, track name, artist name, and uri (link from spotify api)
    dfCopy = dfCopy.drop(["track", "artist", "uri"], axis = 1)
    return dfCopy

dfnew = preprocess(df)

print(dfnew)
    