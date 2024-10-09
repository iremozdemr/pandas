#iloc: integer based
#loc: label based

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")
df.head()

df.iloc[0:3]
#0 1 2 satırlarını seçer

df.iloc[1,3]
#1. satır 3. sütunu seçer

df.loc[0:3]
#0 1 2 3 satırlarını seçer

df.loc[0:3,"age"]
#0 1 2 3 satırlarını age sütunundan seçer

columns = ["age","embarked","alive"]
df.loc[0:3,columns]
#0 1 2 3 satırlarını sütunlardan seçer