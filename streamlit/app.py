import streamlit as st
import pandas as pd
import psycopg2
import os

# Connexion à PostgreSQL
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_DB = os.getenv("POSTGRES_DB", "mydatabase")
POSTGRES_USER = os.getenv("POSTGRES_USER", "myuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "mypassword")

def get_data():
# Connexion à la base de données
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=5432
    )

# Charger les données
    query = "SELECT * FROM data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Afficher les données dans l'interface Streamlit
st.title("Données stockées dans PostgreSQL")
st.write("Données stockées dans PostgreSQL :")

df = get_data()
st.dataframe(df)
