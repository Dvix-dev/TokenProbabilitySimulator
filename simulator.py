# Imports
import random

# Variables
sack = 137500
specialnum = 67
cont = 0

print("""
TOKEN SIMULATOR
""")

while True:
    opc1 = int(input("""
    1. Tirar
    2. Cuantas veces salio
    3. Reset
    0. Salir
    
    Selecciona opción: """))

    if opc1 == 1:
        veces = int(input("Cuantas veces: "))
        contadorinterno = 0
        for i in range(veces):
            numero = random.randint(1, sack)
            if numero == specialnum:
                contadorinterno += 1
        cont += contadorinterno
        if (contadorinterno == 0):
            print("Estas shope y no te has comido una mierda")
        else:
            print(f"En esas {veces} tiradas te hubiesen salido {contadorinterno} tokens")

    elif opc1 == 2:
        print(f"Ha salido {cont}")

    elif opc1 == 3:
        cont = 0
        print("Contador global reseteado a 0")

    elif opc1 == 0:
        break