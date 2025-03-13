CREATE TABLE if not exists data (
    Id_bien SERIAL PRIMARY KEY,
    No_voie INTEGER,
    Type_voie TEXT,
    Voie TEXT,
    Total_piece INTEGER,
    Surface_carrez FLOAT,
    Surface_total INTEGER,
    Type_local TEXT,
    Id_commune INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
