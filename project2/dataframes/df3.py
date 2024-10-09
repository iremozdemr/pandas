import pandas as pd

pd.options.display.max_rows
#sistemin en fazla kaç satır dönebileceği bilgisini verir
#eğer df bu sayıdan daha fazla satır içeriyorsa:
#ilk 5 satırı
#son 5 satırı döner

pd.options.display.max_rows = 100
#değeri değiştirilebilir

df = pd.read_csv("/project2/data.csv")

print(df.head())

print(df)