import pythonbasics
import app2
import streamlit as st
import pandasbasics

PAGES = {
    "Python Basics": pythonbasics,
    "Numpy Basics": app2,
    "Pandas Basics": pandasbasics


}
st.set_page_config(
    page_title='Datascience cheat sheet',
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown("""
    <style>
    body {
        color: #00628B;
        background-color: #d6ffe8;
    }
    </style>
        """, unsafe_allow_html=True)
st.title("Data Science App")
st.sidebar.header('Data Science App')
st.sidebar.markdown('''
<small>Summary of the [docs](https://docs.streamlit.io/en/stable/api.html), as of [Streamlit v0.71.0](https://www.streamlit.io/).</small>
    ''', unsafe_allow_html=True)
selection = st.sidebar.radio("Choose what you want to learn", list(PAGES.keys()))
page = PAGES[selection]
page.main()
