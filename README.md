# 🎬 Movie Recommendation System

## 📌 Overview
This project is a **Movie Recommendation System** built using Machine Learning.
It recommends movies to users based on **content similarity**.

## 🎯 Objective
To help users discover movies similar to their interests from a large movie dataset.

## 🧠 Approach
- Data preprocessing
- Feature extraction using vectorization
- Cosine similarity
- Content-based filtering

## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## 📂 Project Structure
movie-recommendation-system/
├── app.py
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
├── model/
│   ├── movies.pkl
│   ├── similarity.pkl
│   └── vectorizer.pkl
├── notebooks/
│   └── movies.ipynb
├── requirements.txt
├── README.md
└── .gitignore

## 🚀 How to Run the Project
1. Install dependencies:
   pip install -r requirements.txt

2. Run the script:
   python app.py

## 📊 Dataset
TMDB 5000 Movies Dataset is used for building the recommendation system.
Dataset used: TMDB 5000 Movies (available on Kaggle)

## ✅ Output
The system recommends top 5 similar movies based on the selected movie.
