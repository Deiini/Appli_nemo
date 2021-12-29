def conversion(n):
    if n > 1:
        conversion(n // 2)
    print(n % 2, end='')


#demande à l'utilisateur d'entré un nombre
nbr = int(input("Entrez un nombre décimal"))

conversion(nbr)