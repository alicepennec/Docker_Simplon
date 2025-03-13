import pandas as pd
import psycopg2
from datetime import datetime

# Connexion à la base de données
conn = psycopg2.connect(
    dbname="mydatabase",
    user="myuser",
    password="mypassword",
    host="db",
    port=5432
)
cursor = conn.cursor()

csv_file_path = "./Bien.csv"

df = pd.read_csv(csv_file_path)

# Transformation
df["created_at"] = datetime.now()

# Chargement dans la base de données
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO data (Id_bien, No_voie, Type_voie, Voie, Total_piece, Surface_carrez, Surface_total, Type_local, Id_commune, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (row["Id_bien"], row["No_voie"], row["Type_voie"], row["Voie"], row["Total_piece"], row["Surface_carrez"], row["Surface_total"], row["Type_local"], row["Id_commune"], row["created_at"])
    )
conn.commit()

print("ETL terminé avec succès !")
conn.close()
