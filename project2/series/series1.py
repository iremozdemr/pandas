#pandas = panel data = python data analysis:
#python library
#used for working with datasets

import pandas as pd
#pd = alternate name = alias

pd.__version__

x = pd.Series([1,2,3,4,5])

type(x)
#çıktı:
#<class 'pandas.core.series.Series'>

type(pd.Series([1,2,3,4,5]))
#çıktı:
#<class 'pandas.core.series.Series'>

x
#çıktı:
#0    1
#1    2
#2    3
#3    4
#dtype: int64

x.index
#çıktı:
#RangeIndex(start=0, stop=5, step=1)

x.dtype
#çıktı:
#int64

x.size
#çıktı:
#5

x.ndim
#kaç boyutlu olduğunu verir
#çıktı:
#1

x.values
#çıktı:
#[1 2 3 4 5]

type(x.values)
#çıktı:
#<class 'numpy.ndarray'>

x.head(3)
#ilk 3 elementi verir
#çıktı:
#0    1
#1    2
#2    3
#dtype: int64

x.tail(3)
#son 3 elementi verir
#çıktı:
#2    3
#3    4
#4    5
#dtype: int64