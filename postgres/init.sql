CREATE TABLE IF NOT EXISTS data (
    Id SERIAL PRIMARY KEY,
    Code_bien VARCHAR(20) UNIQUE,
    No_voie INTEGER,
    Type_voie TEXT,
    Voie TEXT,
    Total_piece INTEGER,
    Surface_carrez FLOAT,
    Surface_total INTEGER,
    Type_local TEXT,
    Id_commune INTEGER
);
