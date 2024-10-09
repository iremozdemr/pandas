import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

df.loc[0]
#0. satırı verir

type(df.loc[0])
#series döner
#çıktı:
#pandas.core.series.Series

df.loc[[0,1]]
#0. satırı ve 1. satırı verir

type(df.loc[[0,1]])
#dataframe döner
#çıktı:
#pandas.core.frame.DataFrame