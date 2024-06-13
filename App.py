import streamlit as st
import pandas as pd
import pickle as p
import requests as r

st.title("Movie Recommender System")

f=open("Movie_pkl","rb")
df=p.load(f)
f.close()
movie_list=df["title"].values

f1=open("Similarity_vector","rb")
similar=p.load(f1)
f1.close()

def fetch_poster(movie_id):
    try:
        response=r.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0702652f47a4fd69c4e16eb70861093b&language=en-US")
        data=response.json()
        return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    except:
        response="https://i.pinimg.com/564x/15/f7/11/15f71175edadc2bfb5f373d50804432f.jpg"
        return response

st.title("")
selected_movie_name=st.selectbox("Select the Movie",options=movie_list)

st.title("")
if st.button("Recommend"):
    def movie_reco(movie):
        movie_index = df[df["title"] == movie].index[0]
        distance = similar[movie_index]
        movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]

        reco_poster=[]
        reco_movie=[]
        for i in movie_list:
            reco_movie.append(df.iloc[i[0]]["title"])
            poster=df.iloc[i[0]]["id"]
            reco_poster.append(fetch_poster(poster))
        return reco_movie,reco_poster

    recommended_movie,recommended_poster=movie_reco(selected_movie_name)
    c1,c2,c3=st.columns(3)
    with c1:
        st.image(recommended_poster[0])
        st.text(recommended_movie[0])
        st.text("")
        st.image(recommended_poster[3])
        st.text(recommended_movie[3])
        st.text("")
        st.image(recommended_poster[6])
        st.text(recommended_movie[6])

    with c2:
        st.image(recommended_poster[1])
        st.text(recommended_movie[1])
        st.text("")
        st.image(recommended_poster[4])
        st.text(recommended_movie[4])
        st.text("")
        st.image(recommended_poster[7])
        st.text(recommended_movie[7])
        st.text("")
        st.image(recommended_poster[9])
        st.text(recommended_movie[9])
    with c3:
        st.image(recommended_poster[2])
        st.text(recommended_movie[2])
        st.text("")
        st.image(recommended_poster[5])
        st.text(recommended_movie[5])
        st.text("")
        st.image(recommended_poster[8])
        st.text(recommended_movie[8])




