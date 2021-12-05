import streamlit as st
from PIL import Image
import pathlib
from pathlib import Path
st.set_page_config(layout="wide")
from Pages import home, testPage

PAGES = {
    "Home": home,
    "Test": testPage
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]

page.app()