import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_6664.png")

with col2:
    st.title("Jeet Desai")
    content = """

    Hi, I'm Jeet. I am pursuing MS CS from Loyola Marymount University. I'm currently working as Graduate assitant at LMU. \n
    I have worked as a software engineer before satrting my masters.
    
    """
    st.write(content)
