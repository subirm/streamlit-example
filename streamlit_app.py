import streamlit as st
import pickle

from langchain.llms import OpenAI
from langchain.chains import VectorDBQA


OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)

st.title("ETF Search")

# Get user input
query = st.text_input("Enter your query here")

# Show progress spinner while processing
with st.spinner("Processing..."):
    qa = VectorDBQA.from_chain_type(llm=OpenAI(model_name='gpt-3.5-turbo', temperature=0, openai_api_key=OPENAI_API_KEY), chain_type="stuff", vectorstore=store)
    if query is not None:
        st.write(f"Answer: {qa.run(query)}")
