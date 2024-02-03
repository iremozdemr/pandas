import pandas as pd

#why pandas?
#-flexibility of python
#-working with big data

df = pd.read_csv("pokemon-data.csv")

#print(df)
#print(df.head())
#print(df.tail())

print(df.columns)
#read headers

print(df["Name"])
print(df.Name)
#read a column

print(df[["Name","Attack","Defense"]])
#belirtilen sütunlar

print(df["Name"][0:5])
#0,1,2,3,4 isimleri 

print(df.iloc[2])
#2. satır

print(df.loc[df["Name"] == "Ivysaur"])
#belirtilen isimdeki satır

print(df.describe())
#max-min değerleri

print(df.sort_values("Name"))
#alfabetik sıraya göre sıralar

print(df.sort_values("Name",ascending=False))
#alfabetik sıranın tersine göre sıralar

print(df.sort_values("Speed"))
#en küçükten başlayarak sıralar

print(df.sort_values("Speed",ascending=False))
#en büyükten başlayarak sıralar