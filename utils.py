import pandas as pd
import psycopg2
import streamlit as st

@st.cache_resource
def get_redshift_connection():
    conn = psycopg2.connect(
        dbname='your_db_name',
        user='your_db_user',
        password='your_db_password',
        host='your_db_host',
        port='your_db_port'
    )
    return conn

def execute_query(sql_query):
    conn = get_redshift_connection()
    df = pd.read_sql_query(sql_query, conn)
    conn.close()
    return df
