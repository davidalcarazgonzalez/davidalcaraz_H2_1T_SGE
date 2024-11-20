import matplotlib.pyplot as plt
import numpy as np

def grafico_consumo_promedio_por_edad(encuestas):
    edades = [encuesta['edad'] for encuesta in encuestas]
    bebidas_totales = [
        encuesta['BebidasSemana'] + encuesta['CervezasSemana'] + encuesta['BebidasFinSemana'] +
        encuesta['BebidasDestiladasSemana'] + encuesta['VinosSemana']
        for encuesta in encuestas
    ]

    # Calcular el consumo promedio por edad
    edad_consumo_dict = {}
    for edad, consumo in zip(edades, bebidas_totales):
        if edad in edad_consumo_dict:
            edad_consumo_dict[edad].append(consumo)
        else:
            edad_consumo_dict[edad] = [consumo]

    # Promedio de consumo por edad
    promedios = [np.mean(consumos) for consumos in edad_consumo_dict.values()]
    edades_unicas = list(edad_consumo_dict.keys())

    # Crear gráfico
    plt.bar(edades_unicas, promedios, color='green', alpha=0.7)
    plt.xlabel('Edad')
    plt.ylabel('Consumo Promedio (bebidas)')
    plt.title('Consumo Promedio de Alcohol por Edad')
    plt.show()  # Mostrar el gráfico

def grafico_problemas_salud(encuestas):
    problemas_salud = {
        'PerdidasControl': 0,
        'DiversionDependenciaAlcohol': 0,
        'ProblemasDigestivos': 0,
        'TensionAlta': 0,
        'DolorCabeza': 0
    }

    for encuesta in encuestas:
        if encuesta['PerdidasControl'] == 'SI':
            problemas_salud['PerdidasControl'] += 1
        if encuesta['DiversionDependenciaAlcohol'] == 'SI':
            problemas_salud['DiversionDependenciaAlcohol'] += 1
        if encuesta['ProblemasDigestivos'] == 'SI':
            problemas_salud['ProblemasDigestivos'] += 1
        if encuesta['TensionAlta'] == 'SI':
            problemas_salud['TensionAlta'] += 1
        if encuesta['DolorCabeza'] == 'SI':
            problemas_salud['DolorCabeza'] += 1

    # Graficar los problemas de salud
    problemas = list(problemas_salud.keys())
    cantidades = list(problemas_salud.values())

    plt.bar(problemas, cantidades, color='red', alpha=0.7)
    plt.xlabel('Problemas de Salud')
    plt.ylabel('Cantidad de Casos')
    plt.title('Frecuencia de Problemas de Salud Relacionados con el Consumo de Alcohol')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()  # Mostrar el gráfico

def grafico_consumo_edad(encuestas):
    edades = [encuesta['edad'] for encuesta in encuestas]
    bebidas_totales = [
        encuesta['BebidasSemana'] + encuesta['CervezasSemana'] + encuesta['BebidasFinSemana'] +
        encuesta['BebidasDestiladasSemana'] + encuesta['VinosSemana']
        for encuesta in encuestas
    ]

    # Graficar consumo total por edad
    plt.scatter(edades, bebidas_totales, color='blue', alpha=0.6)
    plt.xlabel('Edad')
    plt.ylabel('Consumo Total de Alcohol (bebidas)')
    plt.title('Consumo Total de Alcohol por Edad')
    plt.show()  # Mostrar el gráfico
