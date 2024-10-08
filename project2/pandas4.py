#indeksler değişkene çevrilebilir
#değişkenler indekse çevrilebilir

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

df.head()

df.index

df[0:13]

df.drop(1,axis=0).head()
#1. indeks silinir
#kalıcı olarak silinmez

delete_indexes = [1,3,5]
df.drop(delete_indexes,axis=0).head()
#listedeki indeksler silinir
#kalıcı olarak silinmez

delete_indexes = [2,4,6]
df = df.drop(delete_indexes,axis=0)
#kalıcı olarak silinir

delete_indexes = [3,5,7]
df = df.drop(delete_indexes,axis=0,inplace=True)
#kalıcı olarak silinir

#değişkeni indekse çevirme:

df = sns.load_dataset("titanic")

df["age"].head()
df.age.head()
#seçme işlemi

df.index = df.age
#age isimli değişken indeks olarak kullanılır

df = df.drop("age",axis=1)
print(df)
#age isimli değişken sütunlardan silinir

#indeksi değişkene çevirme:

df = sns.load_dataset("titanic")

df["my_variable"] = df.index
#my_variable isimli değişken yoksa değişken oluşturulur
#indeks değeri değişkene atanır

df.reset_index()
#indeks olarak belirlenen değişken silinir