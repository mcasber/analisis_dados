import random
import matplotlib.pyplot as plt

def main(numero_de_intentos):
    tiros = []
    
    for _ in range(numero_de_intentos):
        dado1 = random.choice([1, 2, 3, 4, 5, 6])
        dado2 = random.choice([1, 2, 3, 4, 5, 6])
        tiros.append(dado1+dado2)

    suma_2 = 0    
    suma_3 = 0
    suma_4 = 0
    suma_5 = 0
    suma_6 = 0
    suma_7 = 0
    suma_8 = 0
    suma_9 = 0
    suma_10 = 0
    suma_11 = 0
    suma_12 = 0

    for i in tiros:
        if i == 2:
            suma_2 +=1
        elif i == 3:
            suma_3 +=1
        elif i == 4:
            suma_4 +=1
        elif i == 5:
            suma_5 +=1
        elif i == 6:
            suma_6 +=1
        elif i == 7:
            suma_7 +=1
        elif i == 8:
            suma_8 +=1
        elif i == 9:
            suma_9 +=1
        elif i == 10:
            suma_10 +=1
        elif i == 11:
            suma_11 +=1
        elif i == 12:
            suma_12 +=1

    prob_2 = suma_2 / numero_de_intentos
    prob_3 = suma_3 / numero_de_intentos
    prob_4 = suma_4 / numero_de_intentos
    prob_5 = suma_5 / numero_de_intentos
    prob_6 = suma_6 / numero_de_intentos
    prob_7 = suma_7 / numero_de_intentos
    prob_8 = suma_8 / numero_de_intentos
    prob_9 = suma_9 / numero_de_intentos
    prob_10 = suma_10 / numero_de_intentos
    prob_11 = suma_11 / numero_de_intentos
    prob_12 = suma_12 / numero_de_intentos

    print(f'Probabilidad de obtener un 7 con DOS dados en {numero_de_intentos} tiros es = {prob_7}')
    print(f'Probabilidad de obtener un 9 con DOS dados en {numero_de_intentos} tiros es = {prob_9}')

    y=[prob_2,prob_3,prob_4,prob_5,prob_6,prob_7,prob_8,prob_9,prob_10,prob_11,prob_12]
    x=[2,3,4,5,6,7,8,9,10,11,12]
    plt.plot(x,y, 'bs-')
    print(plt.show())

if __name__ == '__main__':
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))
    main(numero_de_intentos)
