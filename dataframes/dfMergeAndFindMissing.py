import datetime as dt
import time
import pause
import pandas as pd
import sys

df1 = pd.DataFrame({'A':list('abcde')})
df2 = pd.DataFrame({'A':list('cdefgh')})

print(df1, '\n')
print(df2)

df = (
    df1.merge(df2,
              on='A',
              how='outer',
              indicator=True)
    .query('_merge != "both"')
    .drop(columns='_merge')
)

print('\n', df)
