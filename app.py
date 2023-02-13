import streamlit as st
import pandas as pd 
import plotly.express as px

import buildup

@st.cache_data
def get_data()->dict:
    return buildup.main()

@st.cache_data
def get_options(corpus:dict)->dict:
    return buildup.get_options(corpus)

data = get_data()
categories, sub_categories = get_options(data)

def build_category_options(cats:list):
    while len(cats)>0:
        c = cats.pop()
        yield st.sidebar.checkbox(c)

super_choice = st.sidebar.selectbox('Choose a Category', options=['']+categories)

if super_choice != '':
    st.sidebar.multiselect("Select Line Items",options=sub_categories[super_choice])

def agg_data(*args, corpus)->pd.DataFrame:
    """pass a list of selected options underneath a category, return a dataframe"""
    
st.write(get_data())







# st.write(categories, sub_categories)
