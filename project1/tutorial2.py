import pandas as pd

df = pd.read_csv("pokemon-data.csv")

df["Total"] = df["HP"]+df["Attack"]+df["Defense"]+df["Speed"]
#sütunları toplama

print(df["Total"])
print(df[["Name","Total"]])

df = df.drop(columns="Type 1")
#Type 1 sütununu data frameden siler
df = df.drop(columns=["Type 2","Sp. Atk","Sp. Def","Generation","Legendary"])
#belirtilen sütunları data frameden siler

print(df.head())

df.to_csv("modified.csv")
#verinin yeni halini csv olarak kaydeder