import pandas as pd
import numpy as np
import streamlit as st


df_anime = pd.read_csv('Data/anime_adj.csv')

def get_categories():
    categories = []
    for i in df_anime.index:
        category = df_anime.loc[i,'item_genre'].split(',')
        for j in range(len(category)):
            categories.append(category[j].strip())
    categories = pd.Series(categories).value_counts().index.to_list()
    categories.insert(0,"All")
    return categories 

def print_rec(top_k,df):
    for i in range(top_k):
        rec_title = df.iloc[i]["item_name"]
        rec_avg_rating = df.iloc[i]["item_avg_rating"]
        rec_genre = df.iloc[i]["item_genre"]

        # divide the page into 2 columns
        col1, col2 = st.columns(2)

        # print the attributes on the page
        with col1:
            st.write(rec_title)
        with col2:
            st.write(rec_avg_rating)
            st.write(rec_genre)
   