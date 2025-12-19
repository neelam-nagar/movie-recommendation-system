import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

movies = pd.read_csv("movies.csv")

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)

st.markdown("<h1 style='text-align:center;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#9ca3af;'>Find movies similar to what you love</p>", unsafe_allow_html=True)
st.markdown("---")

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "🎥 Select a movie",
    movie_list,
    index=None,
    placeholder="Select a movie"
)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

if st.button("✨ Recommend Movies"):
    if selected_movie is None:
        st.warning("Please select a movie first")
    else:
        st.subheader("🍿 Recommended Movies")
        for m in recommend(selected_movie):
            st.success(m)

st.markdown("<div style='text-align:center;color:gray;'>Made by Neelam Nagar</div>", unsafe_allow_html=True)
