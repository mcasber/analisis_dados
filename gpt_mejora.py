import random
import csv
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(BASE_DIR, 'archivos', 'basedados.csv')

def main(numero_de_intentos):
    tiros = [random.choice([1, 2, 3, 4, 5, 6]) + random.choice([1, 2, 3, 4, 5, 6]) for _ in range(numero_de_intentos)]

    conteo_sumas = {suma: tiros.count(suma) for suma in range(2, 13)}

    probabilidades = [conteo_sumas[suma] / numero_de_intentos for suma in range(2, 13)]
    x = list(range(2, 13)) #creo las referencia del eje x para el grafico
    
    # Guardar probabilidades en CSV
    guardar_probabilidades_en_csv(probabilidades, ruta)

    print(f'Probabilidad de obtener un 7 con DOS dados en {numero_de_intentos} tiros es = {probabilidades[5]}')
        
    # GRAFICA
    plt.style.use('bmh')
    plt.plot(x, probabilidades, color='blue', alpha=0.5, linewidth=2, label='dos dados')
    plt.title(f'Simulacion de tiro con dos dados en {numero_de_intentos} lanzamientos')
    plt.xlabel('suma de los 2 dados')
    plt.ylabel('Probabilidad')
    plt.legend()
    plt.show()

def guardar_probabilidades_en_csv(probabilidades, nombre_archivo='basedados.csv'):
    with open(nombre_archivo, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(probabilidades)

if __name__ == '__main__':
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))
    main(numero_de_intentos)