import numpy as np
import pandas as pd

my_index = ['A', 'B', 'C']
my_colums = ['이름', '나이', '성별']
my_data = np.array([['Alice', 'Bob', '홍길동'],
                       [25, 30, 26],
                       ['남', '여', '남']])
df = pd.DataFrame(my_data, index=my_index, columns=my_colums)
# print(df[['나이', '이름']])

print(df, "\n", df.loc["A"])
