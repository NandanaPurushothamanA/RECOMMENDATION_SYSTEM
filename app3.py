import streamlit as st
import pickle


movie = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movies_list = movie['title'].values


st.set_page_config(page_title="Movie Recommendation System", layout="wide")
st.markdown("<h1 style='text-align: center; color: #FF6347;'>🎬 Movie Recommendation System</h1>",
            unsafe_allow_html=True)
st.markdown("---")

selected_movie = st.selectbox("📽️ Select a movie :", movies_list)


def recommend(movies):
    index = movie[movie['title'] == movies].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movies = []
    for i in distance[1:6]:  # skip the first (same movie)
        recommend_movies.append(movie.iloc[i[0]].title)
    return recommend_movies


if st.button("Show Recommendations"):
    recommended = recommend(selected_movie)

    st.markdown("### Top 5 Recommendations:")
    st.markdown("---")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(f"🎬 **{recommended[0]}**")
    with col2:
        st.markdown(f"🎬 **{recommended[1]}**")
    with col3:
        st.markdown(f"🎬 **{recommended[2]}**")
    with col4:
        st.markdown(f"🎬 **{recommended[3]}**")
    with col5:
        st.markdown(f"🎬 **{recommended[4]}**")

    st.markdown("---")

