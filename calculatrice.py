#calculatrice
first_number = int(input("Quel est la première valeur ?   "))
operator = input("Quel est l'opération à faire ?   ")
second_number = int(input("Quel est la deuxième valeur ?   "))

#On vérifie qu'on as bien deux chiffres ou nombres et un opérateur.
if first_number == "":
    first_number = input(int("Il est nécessaire de me donner un nombre ?   ") )

elif operator == "":
    operator = input("Il est nécessaire de me donner un opérateur ! exemple : + , - , * , / ")

elif second_number == "":
    second_number = input(int("Quel est le deuxième nombre ?   "))
    
#On vérifie et on positionne le bon opérateur et on affiche le résultât.
if operator == "+":
    result_addition = first_number + second_number
    print(result_addition)

elif operator == "-":
    result_soustraction = first_number - second_number
    print(result_soustraction)
    
elif operator == "*":
    result_multiplication = first_number * second_number
    print(result_multiplication)
    
elif operator == "/":
    result_division = first_number // second_number
    print(result_division)
