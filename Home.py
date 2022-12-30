import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("images/IMG_6664.png")

with col2:
    st.title("Jeet Desai")
    content = """
    Hi, I'm Jeet. I am pursuing MS CS from Loyola Marymount University. I'm currently working as Graduate assitant at LMU.
    I have worked as a software engineer before satrting my masters. 
    """

    st.info(content)

content2 = """

Below you can find  some of the apps I have built. Feel free to contact me!

"""
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[source code](https://github.com/JEETDESAI25?tab=repositories)")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[source code](https://github.com/JEETDESAI25?tab=repositories)")
