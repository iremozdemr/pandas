import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns",None)
#tüm değişkenleri seçmek için yapılan ayar

df = sns.load_dataset("titanic")

df["age"].head()

print(type(df[["age"]].head()))
#seçimin sonucu:
#dataframe
#çıktı:
#<class 'pandas.core.frame.DataFrame'>

print(type(df["age"].head()))
#seçimin sonucu:
#pandas series
#çıktı:
#<class 'pandas.core.series.Series'>

df.age.head()

print(type(df.age.head()))
#seçimin sonucu:
#pandas series
#çıktı:
#<class 'pandas.core.series.Series'>

df[["age","alive"]].head()
print(type(df[["age","alive"]].head()))

column_names = ["age","adult_male","alive"]
df[column_names].head()
print(df[column_names].head())

print("age" in df)
#bir değişkenin olup olmadığını kontrol etme

df["new_age"] = df["age"]**2
print(df.columns)
#değişken ekleme

df = df.drop("new_age",axis=1)
print(df.columns)
#değişken silme

delete_list = ["age","adult_male","alive"]
df = df.drop(delete_list,axis=1)
print(df.columns)
#değişken silme