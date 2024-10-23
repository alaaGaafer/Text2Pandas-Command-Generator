import streamlit as st
import pandas as pd
import re
import os
import time
from dotenv import load_dotenv
from spellchecker import SpellChecker
import google.generativeai as genai
from FewShotExamples import few_shot_examples

# Initialize spell checker
spell = SpellChecker()

# Initialize the Google API
def setup():
    try:
        load_dotenv('API.env')
        gemini_api_key = os.getenv('GEMINI_API_KEY')
        
        if gemini_api_key is None:
            raise Exception("GEMINI_API_KEY is not set")
            
        genai.configure(api_key=gemini_api_key)
        
    except Exception as exception:
        st.error(f"An error occurred during setup: {exception}")

# Correct spelling mistakes and ignore the column names 
def correct_spelling(query, ignore_words=[]):
    words = query.split()
    corrected_query = []
    
    for word in words:
        if word in ignore_words:
            corrected_query.append(word)
        else:
            correction = spell.correction(word)
            corrected_query.append(correction if correction else word)
    
    return ' '.join(corrected_query)

# Remove punctuation and special characters
def remove_punctuation(query):
    pattern = r'[!@#$%^?<>;:\~`,]'
    return re.sub(pattern, '', query)

# Remove stopwords
def remove_stopwords(query):
    stopwords = {"the", "to"}
    words = query.split()
    return ' '.join(word for word in words if word not in stopwords)

def preprocess_query(query, ignore_words):
    query = query.lower()
    query = correct_spelling(query, ignore_words)
    query = remove_punctuation(query)
    query = remove_stopwords(query)
    return query

# Function to generate text by Gemini
def generate_text(query, df):
    try:
        column_names = df.columns.tolist()
        query = preprocess_query(query, column_names)

        prompt = f"""
        You are a data analysis assistant. Your task is to translate the following natural language query into a pandas command that operates on a dataframe named 'df'. The dataframe has the following columns: {', '.join(column_names)}.
        Here are some examples to help you understand the difference between different types of queries: {few_shot_examples}.

        Now, given the query:

        Query: "{query}"

        Pandas Command:
        """

        model = genai.GenerativeModel(model_name='gemini-pro')
        response = model.generate_content(prompt)
        command = response.text.strip().replace("```python", "").replace("```", "")
        return command

    except Exception as exception:
        st.error(f"An error occurred during text generation: {exception}")
        return ""

# Function to execute the generated command
def execute_command(command, df):
    try:
        result = eval(command, {'df': df})
        return result
    except Exception as e:
        st.error(f"Error evaluating command: {e}")
        return None

# Streamlit interface
st.title("Text2Pandas Command Generator")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("DataFrame:")
    st.dataframe(df)

    # Input for query
    query = st.text_input("Enter your query:")
    
    if st.button("Generate Command"):
        setup()
        
        if query:
            command = generate_text(query, df)
            if command:
                st.write("Generated Pandas command:")
                st.code(command)

                # Execute the command and display results
                result = execute_command(command, df)
                if result is not None:
                    st.write("Command execution result:")
                    st.write(result)
