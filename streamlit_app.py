from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.title("LangChain App")

# Get user input
query = st.text_input("Enter your query here")

# Show progress spinner while processing
with st.spinner("Processing..."):
    # Call LangChain API to get answer
    # answer = lc.answer(query)
    # Show the answer
    st.write(f"Answer: {query}")
    
        
        

