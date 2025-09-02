numero = int(input("Ingrese el numero de terminos:"))
if numero <= 0:
    print("No se imprime nigun termino.")
elif numero == 1:
    print(0)
else:
    a = 0
    b = 1
    print(a)
    print(b)
    cont = 1
    while cont <= (numero - 2):
        siguiente = a + b
        print(siguiente)
        a = b
        b = siguiente
        cont += 1