import pandas as pd

df = pd.read_csv('final1.csv')
# del df['title_x']
# del df['title_y']
# del df['id1']
# del df['level_0']
#del df['index']
# del df['overview']

df.to_csv('final.csv')