import pandas as pd
data = {
        '이름': ['Alice', 'Bob', '홍길동'],
        '나이': [25, 30, 26],
        '성별': ['여', '남', '남']
}

df = pd.DataFrame(data, index=['A', 'B', 'C'])
df.to_csv("./data.csv")
print(df)