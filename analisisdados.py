import random

def grandes_numeros(experimentos):

    total=0

    for i in range(experimentos):
        dado1=random.randint(1,6)
        dado2=random.randint(1,6)
        resultado=dado1+dado2
        total+=resultado
    return total/experimentos

random.seed(10)#semilla

pruebas=(1,10,100,1000,10000,100000,1000000,10000000)

for i in range(len(pruebas)):

    experimentos=pruebas[i]
    print(f'El valor promedio esperado con {pruebas[i]} pruebas es de: {grandes_numeros(experimentos)}')
