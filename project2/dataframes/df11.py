#aggregation = toplulaştırma
#gruplama = grouping

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean()
#çıktı:
#29.69911764705882
#yaş ortalaması alınır

df.groupby("sex")["age"].mean()
#çıktı:
#female    27.915709
#male      30.726645
#cinsiyete göre gruplandırılır
#yaş ortalaması alınır

df.groupby("sex").agg({"age":"mean"})
#çıktı:
#female    27.915709
#male      30.726645

column_list = ["mean","sum"]
df.groupby("sex").agg({"age":column_list})
#çıktı:
#female  27.915709   7286.00
#male    30.726645  13919.17