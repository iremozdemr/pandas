import pandas as pd
from sphinx.addnodes import index

#list kullanarak seri oluşturma:
x = [1,2,3,4,5]
pd.Series(x)

#dictionary kullanarak seri oluşturma:
calories = {"day1": 420, "day2": 380, "day3": 390}
pd.Series(calories)
#tüm veriler kullanılırak seri oluşturulur
pd.Series(calories,index=["day1","day2"])
#sadece day1 ve day2 kullanılırak seri oluşturulur

a = pd.Series([8, 7, 2],index=["aa","bb","cc"])
#label oluşturma

a[0]
#çıktı: 8

a["aa"]
#çıktı: 8