import pandas as pd
import numpy as np
import os
import psycopg2
from datetime import datetime

# Récupération des variables d’environnement
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_DB = os.getenv("POSTGRES_DB", "mydatabase")
POSTGRES_USER = os.getenv("POSTGRES_USER", "myuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "mypassword")

# Connexion à la base de données
try:
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=5432
    )
    cursor = conn.cursor()
    print("✅ Connexion PostgreSQL réussie !")
except Exception as e:
    print(f"❌ Erreur de connexion à PostgreSQL: {e}")
    exit(1)

csv_file_path = "./Bien.csv"

try:
    df = pd.read_csv(csv_file_path, sep=';')
    print(df.columns)
    print(df.head())
    df = df.replace({np.nan: None})
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO data (Code_bien, No_voie, Type_voie, Voie, Total_piece, Surface_carrez, Surface_total, Type_local, Id_commune) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row["Id_bien"], row["No_voie"], row["Type_voie"], row["Voie"], row["Total_piece"], row["Surface_carrez"], row["Surface_total"], row["Type_local"], row["Id_commune"])
        )
    conn.commit()
    print("✅ Données insérées avec succès !")
except Exception as e:
    print(f"❌ Erreur lors de l'insertion des données: {e}")

cursor.close()
conn.close()
