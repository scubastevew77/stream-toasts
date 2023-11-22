import streamlit as st

if st.button("just make some toasts"):
    st.toast("Hi there, here is my toast-1")

if st.button("make some toasts and rerun"):
    st.toast("Hi there, here is my toast-2")
    st.experimental_rerun()
