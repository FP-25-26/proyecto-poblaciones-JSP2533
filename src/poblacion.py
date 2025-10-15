from collections import namedtuple
import csv
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    poblaciones = []
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)

        for pais, codigo, año, censo in lector:
            try:
                año = int(año)
                censo = int(censo)
                poblaciones.append(RegistroPoblacion(pais, codigo, año, censo))
            except ValueError:
                
                continue

    return poblaciones




def calcula_paises(poblaciones):
    lista =[]
    poblaciones.sort(key = lambda r: r.pais)
    for e in poblaciones:
        lista.append(e)
    return lista
print(calcula_paises(lee_poblaciones("data/population.csv")))


def filtra_por_pais(poblaciones, nombre_o_codigo):
    filtra_por_pais(lee_poblaciones("data/population.csv"))



#def filtra_por_paises_y_anyo(poblaciones, anyo, paises):




#def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):