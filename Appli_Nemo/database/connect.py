import sqlite3

c = sqlite3.connect('file:database?mode=rw', uri=True)
curseur = c.cursor()

consult = ' SELECT * FROM achats '

curseur.execute(consult)
resultat = curseur.fetchall()

print(resultat)
c.close()
