import streamlit as st

st.write("Streamlit version:", st.__version__)
st.write("Has experimental_rerun?", hasattr(st, "experimental_rerun"))
