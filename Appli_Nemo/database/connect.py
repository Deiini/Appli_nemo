import sqlite3


def consultation_database():
    conn = sqlite3.connect('file:database/database?mode=rw', uri=True)

    curseur = conn.cursor()
    curseur.execute('SELECT * FROM achats')
    rows = curseur.fetchall()
    conn.close()
    return rows


def enregistrer_achat(matiere_premieres, quantite, prix, ):
    total = (int(quantite)) * (int(prix))

    conn = sqlite3.connect('file:database/database?mode=rw', uri=True)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO achats (matiere_premieres, quantite, prix, total) VALUES (?, ?, ?, ?)',
                   (matiere_premieres, quantite, prix, total))
    conn.commit()
    conn.close()
