import csv
import pandas as pd
from flask import Flask, jsonify, request
import itertools as it

from demo_filtering import output as dfi
from content_filtering import get_recom as cfi

all_movies = []
not_watched = []
liked = []
disliked = []

with open('final.csv', encoding='utf8') as f:
  reader = csv.reader(f)
  data = list(reader)
  all_movies = data[1:]

#print(data)

app = Flask(__name__)
@app.route('/')

def start():
  return 'Welcome to Movie Recommendation System'

@app.route('/get-movies')
def get_movies():
  d = {
    'original_title': all_movies[0][7],
    'imdb_link': all_movies[0][24],
    'release_date': all_movies[0][12], 
    'runtime': all_movies[0][14], 
    'vote_average': all_movies[0][18]
  }
  return jsonify({
    'Data': d,
    'Status': 'Success'
  })

@app.route('/liked-movies', methods=['POST'])
def liked_movies():
  movie = all_movies[0]
  movies = all_movies[1:]
  liked_movies.append(movie)
  return jsonify({
    'Data': movie,
    'Status': 'Success'
  })

@app.route('/disliked-movies', methods=['POST'])
def disliked_movies():
  movie = all_movies[0]
  movies = all_movies[1:]
  disliked_movies.append(movie)
  return jsonify({
    'Data': movie,
    'Status': 'Success'
  })

@app.route('/not_watched-movies', methods=['POST'])
def not_watched_movies():
  movie = all_movies[0]
  movies = all_movies[1:]
  not_watched_movies.append(movie)
  return jsonify({
    'Data': movie,
    'Status': 'Success'
  })

@app.route('/popular-movies')
def popular_movies():
  movie_data = []
  for movie in dfi:
    d = {
      'original_title': movie[0],
      'imdb_link': movie[1],
      'release_date': movie[2], 
      'runtime': movie[3], 
      'vote_average': movie[4]
    }
    movie_data.append(d)
  return jsonify({
    'Data': movie_data,
    'Status': 'Success'
  })

@app.route('/recommended-movies')
def recommended_movies():
  all_recommended = []
  for movie in liked:
    output = cfi(movie[7])
    for data in output:
      all_recommended.append(data)
  all_recommended.sort()
  all_recommended = list(all_recommended for all_recommended, _ in it.groupby(all_recommended))
  movie_data = []
  for movie in all_recommended:
    d = {
      'original_title': movie[0],
      'imdb_link': movie[1],
      'release_date': movie[2], 
      'runtime': movie[3], 
      'vote_average': movie[4]
    }
    movie_data.append(d)
  return jsonify({
    'Data': movie_data,
    'Status': 'Success'
  })

if(__name__ == '__main__'):
  app.run(debug=True)