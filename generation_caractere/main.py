import random
import string

def getPassword(length):
    """Générer une chaine de caractere aléatoire"""
    str = string.ascii_lowercase
    return  ''.join(random.choice(str) for i in range(length))

print("La chaine est la suivante ;",getPassword(8) )