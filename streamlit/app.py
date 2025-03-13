import streamlit as st
import pandas as pd
import psycopg2

# Connexion à la base de données
conn = psycopg2.connect(
    dbname="mydatabase",
    user="myuser",
    password="mypassword",
    host="db",
    port=5432
)

# Charger les données
query = "SELECT * FROM data"
df = pd.read_sql(query, conn)

# Afficher les données dans l'interface Streamlit
st.title("Données stockées dans PostgreSQL")
st.write(df)
