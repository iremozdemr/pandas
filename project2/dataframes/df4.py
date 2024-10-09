import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

print(df.head())
print(df.tail())

print(df.shape)
#kaç satır ve kaç sütun olduğu bilgisini verir
#çıktı: 
#(891, 15)

print(df.info())
#genel bilgi verir

print(df.columns)

print(df.index)

print(df.describe())

print(df.describe().T)

print(df.isnull().sum())
#tüm column'lardaki null sayıları

print(df["sex"].head())

print(df["sex"].value_counts())
#hangi veriden kaç tane bulunduğunu gösterir