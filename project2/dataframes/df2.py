import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

df.loc["day1"]
df.loc["day2"]
df.loc["day3"]
#doğru

#df.loc[0]
#df.loc[1]
#df.loc[2]
#yanlış