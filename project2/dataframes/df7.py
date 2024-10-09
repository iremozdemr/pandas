import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

df["age2"] = df["age"]**2
df["age3"] = df["age"]/2
df["age4"] = df["age"]+5

print(df.columns)

df = df.loc[:,~df.columns.str.contains("age")]

print(df.columns)