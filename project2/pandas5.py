import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns",None)
#tüm değişkenleri seçmek için yapılan ayar

df = sns.load_dataset("titanic")
print(df)

print("age" in df)
#bir değişkenin olup olmadığını kontrol etme

print(df["age"].head())
print(type(df["age"].head()))
#çıktı:
#<class 'pandas.core.series.Series'>

print(df.age.head())
print(type(df.age.head()))
#çıktı:
#<class 'pandas.core.series.Series'>