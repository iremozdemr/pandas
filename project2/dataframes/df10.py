import pandas as pd
import numpy as np

data = {
    'StudentID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 21, 22, 20, 23],
    'Major': ['Math', 'Physics', 'Chemistry', 'Math', 'Biology'],
    'GPA': [3.5, 3.7, 2.9, 3.8, 3.2]
}

df = pd.DataFrame(data)
#dict -> dataframe dönüşümü

df.head()

type(data)
#çıktı:
#dict
type(df)
#çıktı:
#pandas.core.frame.DataFrame

df[df['GPA'] == 3.2]
#gpa = 3.2 olan satırı seçer

df[(df['GPA'] > 3.5) & (df['Age'] == 21)]
#birden fazla koşul varsa parantez mutlaka kullanılmalıdır

df[['Name', 'GPA']]
#name ve gpa sütunlarını seçer

df.filter(items=['Name', 'GPA'])
#name ve gpa sütunlarını seçer

df.loc[df["GPA"] < 3.0, "Status"] = "dusuk_basari"
#dusuk_basari yazılmayan yerlere NaN yazılır

df.loc[df["GPA"] < 3.0, "Status"] = "dusuk_basari"
df.loc[df["GPA"] >= 3.0, "Status"] = "yuksek_basari"

df["Status"] = np.where(df["GPA"] < 3.0,"dusuk_basari","yuksek_basari")

majors = ['Math', 'Biology']
df[df["Major"].isin(majors)]
#math veya biology major'ı olan satırları seçer

df.query('GPA >= 3.0 and GPA <= 3.5')

df[df["GPA"].isna()]
#NaN olanları seçer