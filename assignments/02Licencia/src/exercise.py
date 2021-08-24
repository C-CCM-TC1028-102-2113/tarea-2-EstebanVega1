edad= int(input("Ingrese edad:"))
ide= str(input("¿Tiene identificación? (s/n):"))

if edad<0:
    print("Respuesta incorrecta")
elif edad>=18 and ide == "s":
    print("Tramite aceptado")
elif edad<18 and ide == "s":
    print("No cumple con los requisitos")
elif edad>=18 and ide == "n":
    print("No cumple con los requisitos")
elif edad<18 and ide == "n":
    print("No cumple con los requisitos")
elif ide!= "s" or "n":
    print("Respuesta incorrecta")
