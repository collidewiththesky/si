import streamlit as st
import requests
import pandas

df = pd.read_csv('actors.csv')
dfm = pd.read_csv('movies.csv')

actor_names = df['name'].unique()
  actor_selected = st.selectbox("Selecciona un actor", ["Seleccione un actor"] + list(actor_names))
if actor_selected != "Seleccione un actor":
  peliculas = dfm[dfm["name"] == actor_selected
  actor_id = df[df['name'] == movie_selected]['id'].values[0]
  
name_genre = dg_combined["genre"].unique()
        genre_selection = st.selectbox("Seleccione un género", ["Seleccione un género"] + list(name_genre))

        if genre_selection != "Seleccione un género":
            genero_movies = dg_combined[dg_combined["genre"] == genre_selection]["id"].unique()
            filtrar_movies = dm[dm["id"].isin(genero_movies)]
            top10 = filtrar_movies.head(10)

            st.write(f"Top 10 películas de {genre_selection}")

            # Inicializar el índice de películas en la sesión si no existe
            if "movie_index" not in st.session_state:
                st.session_state.movie_index = 0

            col1, col2 = st.columns([17, 1])
