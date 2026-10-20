# Movie Recommendation System

A **content-based** movie recommender built on the top 10,000 TMDB movies. Pick a movie and the Streamlit app suggests the **5 most similar movies**, based on their plot overview and genres.

**Tech stack:** Python · pandas · scikit-learn · Streamlit


## Dataset

`top10K-TMDB-movies.csv` – 10,000 popular movies from TMDB with title, genre, language, overview, popularity, release date and ratings.

## How it works

1. **Feature selection** – kept `id`, `title`, `genre` and `overview`
2. **Tags** – combined each movie's overview and genres into a single text field
3. **Vectorisation** – converted tags into word-count vectors with `CountVectorizer` (10,000 features, English stopwords removed)
4. **Similarity** – computed **cosine similarity** between every pair of movies (10,000 × 10,000 matrix)
5. **Recommendation** – for the selected movie, sort all movies by similarity and return the top 5 (excluding the movie itself)

**Example:** *The Godfather* → *The Godfather: Part II*, *Blood Ties*, *Joker*, *Bomb City*

## Project structure

```
├── recommendationsystem.ipynb   # data preparation, vectorisation, similarity matrix
├── app3.py                      # Streamlit web app
├── top10K-TMDB-movies.csv       # dataset
├── movies_list.pkl              # processed movie list (Git LFS)
├── similarity.pkl               # cosine similarity matrix (Git LFS)
└── README.md
```

## How to run

```bash
pip install pandas scikit-learn streamlit
jupyter notebook recommendationsystem.ipynb   # run all cells to generate the .pkl files
streamlit run app3.py
```

The `.pkl` files are stored with Git LFS. If they don't download correctly when cloning, run the notebook to recreate them.

## Possible improvements

- Use TF-IDF instead of raw counts so common words carry less weight
- Add cast, director and keywords to the tags
- Show movie posters using the TMDB API

