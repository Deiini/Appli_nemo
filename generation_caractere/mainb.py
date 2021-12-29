import random
import string


numbers =str(input("Veuillez entrer le nombre de caractere :"))

def getpassword(length):
    """Générer une chaîne aléatoire de longueur fixe"""
    return ''.join(random.choice(str) for i in range(length))


print("La chaine aleatoire est :", getpassword(length='8'))