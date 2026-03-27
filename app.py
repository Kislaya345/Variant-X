from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai


api_key = os.getenv("GOOGLE_API_KEY") or st.secrets['GOOGLE_API_KEY']
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-2.5-flash')

def my_output(query):
    response = model.generate_content(query)
    return response.text

# UI development

st.set_page_config(page_title='Gemini Variant-X')

st.markdown(
    """
    
    <style>
    
    h2 {
        font-size : 60px !important;
    }
    
    header {
        visibility: hidden;
    }
    
    .stApp{
        background-color: #fafafa;
        color: black;
    }
    
    .stTextInput input{
        background-color: #fafafa;
        color: black;
        border: 2px solid black;
        border-radius: 8px;
    }
    
    .stTextInput label {
        color: black !important;
        margin-top: 1.5rem;
    }
    
    .stButton button,
    .stButton button * {
    background-color: black !important;
    color: white !important;
    border-radius: 8px;
    font-size: 15px;
    border: none;
    }

    .stButton button {
        margin-top: 1.5rem;
        width: 150px;
    }
    
    html, body, .stApp {
        height: 100%;
    }

    .block-container {
    max-width: 70vh;
    margin-left: auto;
    margin-right: auto;
    padding-top: 25vh;
    }
    
    .stButton button,
    .stButton button:hover,
    .stButton button:active,
    .stButton button:focus{
        background-color: black !important;
        color: white !important;
    }
    
    h1, h2, h3, p {
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Gemini's Variant-X")
input = st.text_input("Enter the query to ask:", key="input")
submit = st.button("Generate the Output")

if submit: 
    response = my_output(input)
    st.subheader("The response is =")
    st.write(response)