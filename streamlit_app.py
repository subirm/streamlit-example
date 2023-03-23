import streamlit as st
import pickle
import langchain


from langchain import OpenAI, VectorDBQA


with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
llm_gpt = OpenAI(model_name='gpt-3.5-turbo', temperature=0, openai_api_key=OPENAI_API_KEY)

qa = VectorDBQA.from_chain_type(llm=llm_gpt, chain_type="stuff", vectorstore=store)


st.title("ETF Search")

# Get user input
query = st.text_input("Enter your query here")

# Show progress spinner while processing
with st.spinner("Processing..."):
    if query is not None and string :
        st.write(f"Answer: {qa.run(query)}")
