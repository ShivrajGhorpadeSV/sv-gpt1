import streamlit as st
import openai
import pandas as pd
from utils import execute_query

# Initialize OpenAI API key
openai.api_key = 'your-openai-api-key'

def convert_question_to_sql(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Convert this question into a SQL query: {question}",
        max_tokens=150
    )
    sql_query = response.choices[0].text.strip()
    return sql_query

def main():
    st.title("ChatGPT to Redshift Query App")
    
    user_question = st.text_input("Enter your question:")
    
    if st.button("Submit"):
        if user_question:
            st.write("Converting question to SQL query...")
            sql_query = convert_question_to_sql(user_question)
            st.write(f"Generated SQL Query: {sql_query}")

            st.write("Executing SQL query...")
            try:
                df = execute_query(sql_query)
                st.write("Query Results:")
                st.dataframe(df)
            except Exception as e:
                st.error(f"Error executing query: {e}")
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
