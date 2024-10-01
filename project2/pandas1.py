import pandas as pd

x = pd.Series([1,2,3,4,5])

print(type(x))
#çıktı:
#<class 'pandas.core.series.Series'>

print(type(pd.Series([1,2,3,4,5])))
#çıktı:
#<class 'pandas.core.series.Series'>

print(x)
#çıktı:
#0    1
#1    2
#2    3
#3    4
#dtype: int64

print(x.index)
#çıktı:
#RangeIndex(start=0, stop=5, step=1)

print(x.dtype)
#çıktı:
#int64

print(x.size)
#çıktı:
#5

print(x.ndim)
#kaç boyutlu olduğunu verir
#çıktı:
#1

print(x.values)
#çıktı:
#[1 2 3 4 5]

print(type(x.values))
#çıktı:
#<class 'numpy.ndarray'>

print(x.head(3))
#ilk 3 elementi verir
#çıktı:
#0    1
#1    2
#2    3
#dtype: int64

print(x.tail(3))
#son 3 elementi verir
#çıktı:
#2    3
#3    4
#4    5
#dtype: int64