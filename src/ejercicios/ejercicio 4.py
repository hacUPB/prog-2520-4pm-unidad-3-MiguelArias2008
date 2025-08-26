edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 0:
    if edad <= 5:
        etapa = "Primera Infancia"
    elif edad <= 11:
        etapa = "Infancia"
    elif edad <= 18:
        etapa = "Adolescencia"
    elif edad <= 26:
        etapa = "Juventud"
    elif edad <= 59:
        etapa = "Adultez"
    else:
        etapa = "Persona Mayor (Envejecimiento y Vejez)"
    
    print(f"Tu etapa del ciclo de vida es: {etapa}")
else:
    print("La edad ingresada no es válida.")