# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("CSS Day 3 :)")

st.title("My First StreamLit App")

number = st.slider("pick a number", 1, 10)

st.write(f"you picked {number}")

st.header("heading 1")

st.markdown("some text that you can write")

# st.title("Title heading")

# st.write("Hello, Streamlit!")

# st.header("Number selection")

# number = st.slider("Pick a number", 1, 100)
# st.write(f"You picked: {number}")