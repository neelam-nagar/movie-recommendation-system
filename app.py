import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.movie-card {
    background-color: #1f2933;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    font-size: 16px;
}
.footer {
    text-align: center;
    color: #9ca3af;
    margin-top: 30px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

movies = pickle.load(open("model/movies.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))

st.markdown(
    "<h1 style='text-align:center;'>🎬 Movie Recommendation System</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;color:#9ca3af;'>Find movies similar to what you love</p>",
    unsafe_allow_html=True
)

st.markdown("---")

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "🎥 Select a movie",
    movie_list,
    index=None,
    placeholder="Select a movie to get recommendations"
)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_indices = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
    return [movies.iloc[i[0]].title for i in movie_indices]

if st.button("✨ Recommend Movies"):
    if selected_movie is None:
        st.warning("Please select a movie first 🎬")
    else:
        st.subheader("🍿 Recommended Movies for You")
        recommendations = recommend(selected_movie)
        for rec in recommendations:
            st.markdown(
                f"<div class='movie-card'>🎞️ {rec}</div>",
                unsafe_allow_html=True
            )

st.markdown(
    "<div class='footer'>Made by Neelam Nagar | Machine Learning Project</div>",
    unsafe_allow_html=True
)
