import streamlit as st
import pickle


from langchain import OpenAI, VectorDBQA
from langchain.chains.question_answering import load_qa_chain


with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
llm_gpt = OpenAI(model_name='gpt-3.5-turbo', temperature=0, openai_api_key=OPENAI_API_KEY)
qa_chain = load_qa_chain(llm_gpt, chain_type="stuff")
qa = VectorDBQA(combine_documents_chain=qa_chain, vectorstore=store)


st.title("ETF Search")

# Get user input
query = st.text_input("Enter your query here")

# Show progress spinner while processing
with st.spinner("Processing...")
    if query is not None:
        st.write(f"Answer: {qa.run(query)}")
