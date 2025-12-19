import streamlit as st
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

@st.cache_data
def load_data():
    movies = pd.read_csv("tmdb_5000_movies.csv")
    return movies

movies = load_data()

def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['overview'] = movies['overview'].fillna("")
movies['tagline'] = movies['tagline'].fillna("")

movies['tags'] = (
    movies['genres']
    + movies['keywords']
    + movies['overview'].apply(lambda x: x.split())
    + movies['tagline'].apply(lambda x: x.split())
)

movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))

new_df = movies[['title', 'tags']]

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()
similarity = cosine_similarity(vectors)

st.markdown("<h1 style='text-align:center;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#9ca3af;'>Content-Based Recommendation using TMDB Dataset</p>", unsafe_allow_html=True)
st.markdown("---")

movie_list = new_df['title'].values

selected_movie = st.selectbox(
    "🎥 Select a movie",
    movie_list,
    index=None,
    placeholder="Select a movie"
)

def recommend(movie):
    index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
    return [new_df.iloc[i[0]].title for i in movies_list]

if st.button("✨ Recommend Movies"):
    if selected_movie is None:
        st.warning("Please select a movie first 🎬")
    else:
        st.subheader("🍿 Recommended Movies")
        for m in recommend(selected_movie):
            st.success(m)

st.markdown("<div style='text-align:center;color:gray;'>Made by Neelam Nagar | TMDB Dataset</div>", unsafe_allow_html=True)
