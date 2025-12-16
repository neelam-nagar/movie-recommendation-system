import streamlit as st
import pickle
import pandas as pd

# Load data and similarity matrix
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("🎬 Movie Recommendation System")

# Dropdown me movie titles dikhana
movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie", movie_list)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendations = []
    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)
    return recommendations

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write("### Recommended Movies:")
    for rec in recommendations:
        st.success(rec)