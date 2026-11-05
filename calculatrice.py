print("=== Calculatrice ===")

try:
    a = float(input("Premier nombre : "))
    operation = input("Opération (+, -, *, /) : ")
    b = float(input("Deuxième nombre : "))

    if operation == "+":
        resultat = a + b
    elif operation == "-":
        resultat = a - b
    elif operation == "*":
        resultat = a * b
    elif operation == "/":
        if b == 0:
            resultat = "Erreur : division par zéro"
        else:
            resultat = a / b
    else:
        resultat = "Opération inconnue"

    print("Résultat :", resultat)

except ValueError:
    print("Erreur : tu dois taper un nombre (par exemple 5 ou 3.2).")
    