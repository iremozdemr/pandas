import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")

df[df["age"] > 70]

df[df["age"] > 70].count()
#yanlış

df[df["age"] > 70]["age"].count()
#doğru

df[df["age"] > 70]["class"]

df.loc[df["age"] > 70,"class"]

columns = ["age","class"]
df.loc[df["age"] > 70,columns]
df.loc[df["age"] > 70,["age","class"]]

df.loc[(df["age"] > 70) & (df["sex"] == "male")]

df.loc[(df["age"] > 70) & (df["sex"] == "male"),["age","class"]]