import csv

with open ('new_data.csv', encoding='utf8') as f:
  reader = csv.reader(f)
  data = list(reader)
  headers = data[0]
  all_movies = data[1:]

headers.append('imdb_link')
#print(len(headers))
#print(len(all_movies))

with open ('movie_links.csv', encoding='utf8') as f:
  reader = csv.reader(f)
  data = list(reader)
  all_movie_links = data[1:]


with open ('final.csv', 'a+', encoding='utf8') as f:
  writer = csv.writer(f)
  writer.writerow(headers)

for movie_item in all_movies:
  poster_found = any(movie_item[7] in movie_link_items for movie_link_items in all_movie_links)
  if poster_found:
    for movie_link_items in all_movie_links:
      if movie_item[7] == movie_link_items[0]:
        movie_item.append(movie_link_items[1])
        if (len(movie_item) == 25):
          with open ('final.csv', 'a+', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow(movie_item)