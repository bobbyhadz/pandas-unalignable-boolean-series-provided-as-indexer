# Pandas: Unalignable boolean Series provided as indexer 

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan', 'Ethan'],
    'salary': [175.1, None, 190.3, None, 210.5],
    'experience': [None, None, None, None, None],
})

print(df)

print('-' * 50)

df = df.loc[:, df.notnull().any(axis=0)]

print(df)