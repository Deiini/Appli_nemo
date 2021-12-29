"""
Code qui génére le nombre de suite de Fibonacci demandé
Benjamin PIEL   29/12/2021
"""
nombers = int(input("Please enter a number:  "))
a = 1
b = 2

print("\n The Fibonacci's suit number is :")
print(a, ",", b, end=", ")

for i in range(b, nombers):
    next= a + b
    print(next, end=", ")

    a=b
    b=next