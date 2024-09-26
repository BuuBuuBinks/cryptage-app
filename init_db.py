import psycopg2
import os

# Connexion à la base de données PostgreSQL sur Heroku
conn = psycopg2.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

# Création de la table cles_motsdepasse si elle n'existe pas
cur.execute('''
    CREATE TABLE IF NOT EXISTS cles_motsdepasse (
        cle TEXT PRIMARY KEY,
        mot_de_passe TEXT
    );
''')

# Validation de la transaction
conn.commit()

# Fermeture de la connexion
cur.close()
conn.close()
