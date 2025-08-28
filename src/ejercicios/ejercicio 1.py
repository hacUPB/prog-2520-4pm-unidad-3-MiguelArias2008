
nombre = input ("Por favor ingrese su nombre:")
print("Bienvenido", nombre)

#Calcular el indice de masa corporal
#IMC = peso / estatura**2

#Leer estatura
estatura = input("Ingrese su estatura en metros:")
estatura = float(estatura)
#Leer peso
peso = input("ingrese su peso en kg:")
peso = float(peso)
#Calcular imc
imc = peso / estatura**2
#Mostrar imc
print ("Su IMC = ",imc)

#Si IMC menor que 18.49
if imc < 18.49:
    mensaje = "Peso bajo"
else:
    if 18.5 < imc < 24.99:
        Mensaje = "Peso normal"
    else:
        if 25 < imc < 29.9:
            mensaje = "sobrepeso"
        else:
            if 30 < imc < 39.99:
                Mensaje = "Obesidad"
            else:
                if imc > 40:
                    Mensaje = "obesidad extrema"
print (Mensaje)
