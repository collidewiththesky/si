import streamlit as st
import requests

si = st.text_input('escrive pelikula')
def fetch_poster(movie_id):
  url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc".format(movie_id)
  data = requests.get(url)
  data = data.json()
  poster_path = data['poster_path']
  full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
  return full_path


  
