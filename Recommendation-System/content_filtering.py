import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer as cv
from sklearn.metrics.pairwise import cosine_similarity as cs

df = pd.read_csv('final.csv')
df = df[df['soup'].notna()]

count = cv(stop_words = 'english')
count_matrix = count.fit_transform(df['soup'])
cosin = cs(count_matrix, count_matrix)

df = df.reset_index()
indices = pd.Series(df.index, index=df['original_title'])

def get_recom(title):
  idx = indices[title]
  sim_score = list(enumerate(cosin[idx]))
  sim_score = sorted(sim_score, key=lambda x:x[1], reverse=True)
  sim_score = sim_score[1:11]
  movie_indices = [i[0] for i in sim_score]
  return df[['original_title', 'imdb_link', 'release_date', 'runtime', 'vote_average']].iloc[movie_indices].values.tolist()


output = get_recom('Spider-Man 3')
#print(output)